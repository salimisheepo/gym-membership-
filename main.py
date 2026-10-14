import tkinter as tk
from tkinter import messagebox
from gym import Gym
from member import Member
from trainer import Trainer
from equipment import Equipment
from gym_class import GymClass
from exceptions import GymError, DataFileError


class MainApplication:


    def __init__(self, root):
        self.root = root
        self.root.title('Gym Management System')
        self.root.geometry('700x550')
        self.gym = Gym('Fitness Club')
        self.show_main_menu()


    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


    def show_main_menu(self):
        self.clear_window()
        tk.Label(self.root, text='GYM MANAGEMENT SYSTEM', font=('Arial', 22, 'bold')).pack(pady=20)
        tk.Label(self.root, text=f'Gym: {self.gym.name}', font=('Arial', 12)).pack(pady=5)
        buttons = [('Members', self.show_members), ('Trainers', self.show_trainers), ('Classes', self.show_classes), ('Equipment', self.show_equipment), ('Reports', self.show_reports), ('Save / Load', self.show_file_menu), ('Exit', self.root.destroy)]
        for text, command in buttons:
            tk.Button(self.root, text=text, width=25, height=1, command=command).pack(pady=4)


    def show_members(self):
        self.clear_window()
        tk.Label(self.root, text='MEMBERS', font=('Arial', 20, 'bold')).pack(pady=10)
        self.member_listbox = tk.Listbox(self.root, width=90, height=10)
        self.member_listbox.pack(pady=10)
        self._refresh_member_listbox()
        form = tk.Frame(self.root)
        form.pack(pady=5)
        tk.Label(form, text='Name:').grid(row=0, column=0, sticky='e')
        self.member_name_entry = tk.Entry(form, width=20)
        self.member_name_entry.grid(row=0, column=1)
        tk.Label(form, text='ID:').grid(row=0, column=2, sticky='e')
        self.member_pid_entry = tk.Entry(form, width=10)
        self.member_pid_entry.grid(row=0, column=3)
        tk.Label(form, text='Age:').grid(row=1, column=0, sticky='e')
        self.member_age_entry = tk.Entry(form, width=20)
        self.member_age_entry.grid(row=1, column=1)
        tk.Label(form, text='Phone:').grid(row=1, column=2, sticky='e')
        self.member_phone_entry = tk.Entry(form, width=10)
        self.member_phone_entry.grid(row=1, column=3)
        tk.Label(form, text='Plan:').grid(row=2, column=0, sticky='e')
        self.member_plan_var = tk.StringVar(value='basic')
        tk.OptionMenu(form, self.member_plan_var, 'basic', 'premium', 'vip').grid(row=2, column=1, sticky='w')
        tk.Label(form, text='VIP months:').grid(row=2, column=2, sticky='e')
        self.member_vip_months_entry = tk.Entry(form, width=10)
        self.member_vip_months_entry.insert(0, '0')
        self.member_vip_months_entry.grid(row=2, column=3)
        tk.Button(self.root, text='Add Member', width=20, command=self.add_member_clicked).pack(pady=5)
        tk.Button(self.root, text='Remove Selected Member', width=20, command=self.remove_member_clicked).pack(pady=2)
        tk.Button(self.root, text='Main Menu', width=20, command=self.show_main_menu).pack(pady=10)


    def _refresh_member_listbox(self):
        self.member_listbox.delete(0, tk.END)
        for member in self.gym.members:
            self.member_listbox.insert(tk.END, member.details())


    def add_member_clicked(self):
        try:
            age_text = self.member_age_entry.get()
            vip_months_text = self.member_vip_months_entry.get()
            try:
                age = int(age_text)
            except ValueError:
                raise ValueError(f"Age must be a whole number, got '{age_text}'")
            try:
                vip_months = int(vip_months_text) if vip_months_text else 0
            except ValueError:
                raise ValueError(f"VIP months must be a whole number, got '{vip_months_text}'")
            member = Member(self.member_name_entry.get(), self.member_pid_entry.get(), age, self.member_phone_entry.get(), self.member_plan_var.get(), vip_months=vip_months)
            self.gym.add_member(member)
        except GymError as error:
            messagebox.showerror('Could not add member', str(error))
        except (ValueError, TypeError) as error:
            messagebox.showerror('Invalid input', str(error))
        else:
            self._refresh_member_listbox()
            self.member_name_entry.delete(0, tk.END)
            self.member_pid_entry.delete(0, tk.END)
            self.member_age_entry.delete(0, tk.END)
            self.member_phone_entry.delete(0, tk.END)
            messagebox.showinfo('Success', f'{member.name} added.')


    def remove_member_clicked(self):
        selection = self.member_listbox.curselection()
        if not selection:
            messagebox.showwarning('No selection', 'Select a member to remove first.')
            return
        member = self.gym.members[selection[0]]
        for gym_class in list(member.classes):
            gym_class.remove_member(member)
        self.gym.members.remove(member)
        self._refresh_member_listbox()
        messagebox.showinfo('Removed', f'{member.name} removed.')


    def show_trainers(self):
        self.clear_window()
        tk.Label(self.root, text='TRAINERS', font=('Arial', 20, 'bold')).pack(pady=10)
        self.trainer_listbox = tk.Listbox(self.root, width=90, height=10)
        self.trainer_listbox.pack(pady=10)
        self._refresh_trainer_listbox()
        form = tk.Frame(self.root)
        form.pack(pady=5)
        tk.Label(form, text='Name:').grid(row=0, column=0, sticky='e')
        self.trainer_name_entry = tk.Entry(form, width=20)
        self.trainer_name_entry.grid(row=0, column=1)
        tk.Label(form, text='ID:').grid(row=0, column=2, sticky='e')
        self.trainer_pid_entry = tk.Entry(form, width=10)
        self.trainer_pid_entry.grid(row=0, column=3)
        tk.Label(form, text='Age:').grid(row=1, column=0, sticky='e')
        self.trainer_age_entry = tk.Entry(form, width=20)
        self.trainer_age_entry.grid(row=1, column=1)
        tk.Label(form, text='Phone:').grid(row=1, column=2, sticky='e')
        self.trainer_phone_entry = tk.Entry(form, width=10)
        self.trainer_phone_entry.grid(row=1, column=3)
        tk.Label(form, text='Speciality:').grid(row=2, column=0, sticky='e')
        self.trainer_speciality_entry = tk.Entry(form, width=20)
        self.trainer_speciality_entry.grid(row=2, column=1)
        tk.Button(self.root, text='Add Trainer', width=20, command=self.add_trainer_clicked).pack(pady=5)
        tk.Button(self.root, text='Main Menu', width=20, command=self.show_main_menu).pack(pady=10)


    def _refresh_trainer_listbox(self):
        self.trainer_listbox.delete(0, tk.END)
        for trainer in self.gym.trainers:
            self.trainer_listbox.insert(tk.END, trainer.details())


    def add_trainer_clicked(self):
        try:
            age_text = self.trainer_age_entry.get()
            try:
                age = int(age_text)
            except ValueError:
                raise ValueError(f"Age must be a whole number, got '{age_text}'")
            trainer = Trainer(self.trainer_name_entry.get(), self.trainer_pid_entry.get(), age, self.trainer_phone_entry.get(), self.trainer_speciality_entry.get())
            self.gym.add_trainer(trainer)
        except GymError as error:
            messagebox.showerror('Could not add trainer', str(error))
        except (ValueError, TypeError) as error:
            messagebox.showerror('Invalid input', str(error))
        else:
            self._refresh_trainer_listbox()
            self.trainer_name_entry.delete(0, tk.END)
            self.trainer_pid_entry.delete(0, tk.END)
            self.trainer_age_entry.delete(0, tk.END)
            self.trainer_phone_entry.delete(0, tk.END)
            self.trainer_speciality_entry.delete(0, tk.END)
            messagebox.showinfo('Success', f'{trainer.name} added.')


    def show_classes(self):
        self.clear_window()
        tk.Label(self.root, text='CLASSES', font=('Arial', 20, 'bold')).pack(pady=10)
        self.class_listbox = tk.Listbox(self.root, width=90, height=8)
        self.class_listbox.pack(pady=10)
        self._refresh_class_listbox()
        add_form = tk.Frame(self.root)
        add_form.pack(pady=5)
        tk.Label(add_form, text='Name:').grid(row=0, column=0, sticky='e')
        self.class_name_entry = tk.Entry(add_form, width=15)
        self.class_name_entry.grid(row=0, column=1)
        tk.Label(add_form, text='Schedule:').grid(row=0, column=2, sticky='e')
        self.class_schedule_entry = tk.Entry(add_form, width=15)
        self.class_schedule_entry.grid(row=0, column=3)
        tk.Label(add_form, text='Capacity (blank=unlimited):').grid(row=0, column=4, sticky='e')
        self.class_capacity_entry = tk.Entry(add_form, width=6)
        self.class_capacity_entry.grid(row=0, column=5)
        tk.Button(self.root, text='Add Class', width=20, command=self.add_class_clicked).pack(pady=5)
        action_form = tk.Frame(self.root)
        action_form.pack(pady=10)
        tk.Label(action_form, text='Class name:').grid(row=0, column=0, sticky='e')
        self.action_class_entry = tk.Entry(action_form, width=15)
        self.action_class_entry.grid(row=0, column=1)
        tk.Label(action_form, text='Member/Trainer/Equipment ID or name:').grid(row=0, column=2, sticky='e')
        self.action_target_entry = tk.Entry(action_form, width=15)
        self.action_target_entry.grid(row=0, column=3)
        button_row = tk.Frame(self.root)
        button_row.pack(pady=5)
        tk.Button(button_row, text='Set Trainer (by ID)', command=self.set_trainer_clicked).grid(row=0, column=0, padx=3)
        tk.Button(button_row, text='Enroll Member (by ID)', command=self.enroll_member_clicked).grid(row=0, column=1, padx=3)
        tk.Button(button_row, text='Remove Member (by ID)', command=self.remove_class_member_clicked).grid(row=0, column=2, padx=3)
        tk.Button(button_row, text='Add Equipment (by name)', command=self.add_class_equipment_clicked).grid(row=0, column=3, padx=3)
        tk.Button(self.root, text='View Waiting List', width=20, command=self.view_waiting_list_clicked).pack(pady=5)
        tk.Button(self.root, text='Main Menu', width=20, command=self.show_main_menu).pack(pady=10)


    def _refresh_class_listbox(self):
        self.class_listbox.delete(0, tk.END)
        for gym_class in self.gym.classes:
            self.class_listbox.insert(tk.END, str(gym_class))


    def _find_class_by_name_or_warn(self):
        name = self.action_class_entry.get().strip()
        gym_class = self.gym.find_class(name)
        if gym_class is None:
            messagebox.showwarning('Not found', f"No class named '{name}'.")
        return gym_class


    def add_class_clicked(self):
        try:
            capacity_text = self.class_capacity_entry.get().strip()
            capacity = int(capacity_text) if capacity_text else None
            gym_class = GymClass(self.class_name_entry.get(), self.class_schedule_entry.get(), capacity=capacity)
            self.gym.add_class(gym_class)
        except GymError as error:
            messagebox.showerror('Could not add class', str(error))
        except (ValueError, TypeError) as error:
            messagebox.showerror('Invalid input', str(error))
        else:
            self._refresh_class_listbox()
            self.class_name_entry.delete(0, tk.END)
            self.class_schedule_entry.delete(0, tk.END)
            self.class_capacity_entry.delete(0, tk.END)
            messagebox.showinfo('Success', f'{gym_class.name} added.')


    def set_trainer_clicked(self):
        gym_class = self._find_class_by_name_or_warn()
        if gym_class is None:
            return
        pid = self.action_target_entry.get().strip()
        trainer = next((t for t in self.gym.trainers if t.pid == pid), None)
        if trainer is None:
            messagebox.showwarning('Not found', f"No trainer with ID '{pid}'.")
            return
        try:
            gym_class.set_trainer(trainer)
        except TypeError as error:
            messagebox.showerror('Could not set trainer', str(error))
        else:
            self._refresh_class_listbox()
            messagebox.showinfo('Success', f'{trainer.name} is now training {gym_class.name}.')


    def enroll_member_clicked(self):
        gym_class = self._find_class_by_name_or_warn()
        if gym_class is None:
            return
        pid = self.action_target_entry.get().strip()
        member = next((m for m in self.gym.members if m.pid == pid), None)
        if member is None:
            messagebox.showwarning('Not found', f"No member with ID '{pid}'.")
            return
        try:
            status = gym_class.add_member(member)
        except GymError as error:
            messagebox.showerror('Could not enroll', str(error))
        except (ValueError, TypeError) as error:
            messagebox.showerror('Could not enroll', str(error))
        else:
            self._refresh_class_listbox()
            messages = {'joined': f'{member.name} joined {gym_class.name}.', 'waitlisted': f'{gym_class.name} is full -- {member.name} was added to the waiting list.', 'already_in': f'{member.name} is already in {gym_class.name}.', 'already_waiting': f'{member.name} is already on the waiting list.'}
            messagebox.showinfo('Enrollment', messages.get(status, status))


    def remove_class_member_clicked(self):
        gym_class = self._find_class_by_name_or_warn()
        if gym_class is None:
            return
        pid = self.action_target_entry.get().strip()
        member = next((m for m in self.gym.members if m.pid == pid), None)
        if member is None:
            messagebox.showwarning('Not found', f"No member with ID '{pid}'.")
            return
        gym_class.remove_member(member)
        self._refresh_class_listbox()
        messagebox.showinfo('Removed', f'{member.name} removed from {gym_class.name} (waiting list promoted automatically if anyone was waiting).')


    def add_class_equipment_clicked(self):
        gym_class = self._find_class_by_name_or_warn()
        if gym_class is None:
            return
        eq_name = self.action_target_entry.get().strip()
        item = next((e for e in self.gym.equipment if e.name == eq_name), None)
        if item is None:
            messagebox.showwarning('Not found', f"No equipment named '{eq_name}'.")
            return
        try:
            gym_class.add_equipment(item)
        except TypeError as error:
            messagebox.showerror('Could not add equipment', str(error))
        else:
            self._refresh_class_listbox()
            messagebox.showinfo('Success', f'{item.name} added to {gym_class.name}.')


    def view_waiting_list_clicked(self):
        gym_class = self._find_class_by_name_or_warn()
        if gym_class is None:
            return
        if gym_class.waiting_list.is_empty():
            messagebox.showinfo('Waiting list', f'{gym_class.name} has no one waiting.')
        else:
            names = ', '.join((person.name for person in gym_class.waiting_list.to_list()))
            messagebox.showinfo('Waiting list', f'{gym_class.name} waiting list (front to back): {names}')


    def show_equipment(self):
        self.clear_window()
        tk.Label(self.root, text='EQUIPMENT', font=('Arial', 20, 'bold')).pack(pady=10)
        self.equipment_listbox = tk.Listbox(self.root, width=60, height=10)
        self.equipment_listbox.pack(pady=10)
        self._refresh_equipment_listbox()
        form = tk.Frame(self.root)
        form.pack(pady=5)
        tk.Label(form, text='Name:').grid(row=0, column=0, sticky='e')
        self.equipment_name_entry = tk.Entry(form, width=20)
        self.equipment_name_entry.grid(row=0, column=1)
        tk.Label(form, text='Type:').grid(row=0, column=2, sticky='e')
        self.equipment_type_entry = tk.Entry(form, width=20)
        self.equipment_type_entry.grid(row=0, column=3)
        tk.Button(self.root, text='Add Equipment', width=20, command=self.add_equipment_clicked).pack(pady=5)
        tk.Button(self.root, text='Main Menu', width=20, command=self.show_main_menu).pack(pady=10)


    def _refresh_equipment_listbox(self):
        self.equipment_listbox.delete(0, tk.END)
        for item in self.gym.equipment:
            self.equipment_listbox.insert(tk.END, str(item))


    def add_equipment_clicked(self):
        try:
            item = Equipment(self.equipment_name_entry.get(), self.equipment_type_entry.get())
            self.gym.add_equipment(item)
        except (ValueError, TypeError) as error:
            messagebox.showerror('Invalid input', str(error))
        else:
            self._refresh_equipment_listbox()
            self.equipment_name_entry.delete(0, tk.END)
            self.equipment_type_entry.delete(0, tk.END)
            messagebox.showinfo('Success', f'{item.name} added.')


    def show_reports(self):
        self.clear_window()
        tk.Label(self.root, text='REPORTS', font=('Arial', 20, 'bold')).pack(pady=10)
        tk.Button(self.root, text='Show Average Member Age', width=30, command=self.show_avg_age_clicked).pack(pady=5)
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10)
        tk.Label(search_frame, text='Search by name:').grid(row=0, column=0)
        self.search_entry = tk.Entry(search_frame, width=20)
        self.search_entry.grid(row=0, column=1)
        tk.Button(search_frame, text='Search', command=self.search_clicked).grid(row=0, column=2, padx=5)
        self.search_results_listbox = tk.Listbox(self.root, width=90, height=6)
        self.search_results_listbox.pack(pady=10)
        tk.Button(self.root, text='Show Full Gym Report', width=30, command=self.show_full_report_clicked).pack(pady=5)
        self.report_text = tk.Text(self.root, width=90, height=12)
        self.report_text.pack(pady=10)
        tk.Button(self.root, text='Main Menu', width=20, command=self.show_main_menu).pack(pady=10)


    def show_avg_age_clicked(self):
        messagebox.showinfo('Average Age', f'Average member age: {self.gym.avg_age():.1f}')


    def search_clicked(self):
        self.search_results_listbox.delete(0, tk.END)
        results = self.gym.find_person(self.search_entry.get())
        if not results:
            messagebox.showinfo('Search', 'No matches found.')
        for person in results:
            self.search_results_listbox.insert(tk.END, person.details())


    def show_full_report_clicked(self):
        self.report_text.delete('1.0', tk.END)
        self.report_text.insert(tk.END, self.gym.full_report())


    def show_file_menu(self):
        self.clear_window()
        tk.Label(self.root, text='SAVE / LOAD', font=('Arial', 20, 'bold')).pack(pady=10)
        tk.Label(self.root, text='File path:').pack(pady=5)
        self.file_path_entry = tk.Entry(self.root, width=50)
        self.file_path_entry.insert(0, 'gym_data.json')
        self.file_path_entry.pack(pady=5)
        tk.Button(self.root, text='Save Gym to File', width=25, command=self.save_clicked).pack(pady=5)
        tk.Button(self.root, text='Load Gym from File', width=25, command=self.load_clicked).pack(pady=5)
        tk.Button(self.root, text='Main Menu', width=20, command=self.show_main_menu).pack(pady=10)


    def save_clicked(self):
        filepath = self.file_path_entry.get().strip()
        try:
            self.gym.save_to_file(filepath)
        except DataFileError as error:
            messagebox.showerror('Save failed', str(error))
        else:
            messagebox.showinfo('Saved', f"Gym data saved to '{filepath}'.")


    def load_clicked(self):
        filepath = self.file_path_entry.get().strip()
        try:
            loaded_gym = Gym.load_from_file(filepath)
        except DataFileError as error:
            messagebox.showerror('Load failed', str(error))
        else:
            self.gym = loaded_gym
            messagebox.showinfo('Loaded', f"Gym data loaded from '{filepath}'.")
if __name__ == '__main__':
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
