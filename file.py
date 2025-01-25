import tkinter as tk
from tkinter import messagebox
import os

# وظيفة قراءة الملف وعرض المحتويات
def read_file():
    file_path = entry.get()  # الحصول على النص من الإدخال
    
    if not file_path:
        messagebox.showerror("خطأ", "الرجاء إدخال رابط الملف.")
        return
    
    if not os.path.isfile(file_path):
        messagebox.showerror("خطأ", "الملف غير موجود. الرجاء التحقق من الرابط.")
        return
    
    # إذا كان الملف موجودًا
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # إنشاء نافذة جديدة لعرض المحتويات
    display_window = tk.Toplevel(root)
    display_window.title("محتويات الملف")
    
    text_widget = tk.Text(display_window, wrap='word', width=80, height=25)
    text_widget.insert("1.0", content)
    text_widget.configure(state='disabled')  # منع التعديل على النص
    text_widget.pack(padx=10, pady=10)

# إنشاء نافذة Tkinter
root = tk.Tk()
root.title("قارئ الملفات")

# مكونات الواجهة
label = tk.Label(root, text="أدخل رابط الملف:")
label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

read_button = tk.Button(root, text="اقرأ", command=read_file)
read_button.pack(pady=10)

# تشغيل البرنامج
root.mainloop()
