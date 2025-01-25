import tkinter as tk
from tkinter import messagebox

# البيانات الأساسية
books = []  # قائمة أسماء الكتب
books_details = {}  # قاموس لربط الكتاب بالتفاصيل (عنوان، مؤلف، سنة النشر، تصنيف)
borrowed_books = {}  # قاموس لتخزين الكتب المستعارة (عنوان الكتاب: اسم المستعير)
print("Hello, Python!")

# دالة لإضافة كتاب جديد
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()
    category = category_entry.get()
    
    if title and author and year and category:
        books.append(title)
        books_details[title] = (author, year, category)
        messagebox.showinfo("نجاح", f"تمت إضافة الكتاب: {title} بنجاح!")
        clear_entries()
        display_books()
    else:
        messagebox.showerror("خطأ", "يرجى ملء جميع الحقول!")

# دالة للبحث عن كتاب
def search_books():
    query = search_entry.get().strip()
    if not query:
        messagebox.showerror("خطأ", "يرجى إدخال نص للبحث!")
        return
    
    results_list.delete(0, tk.END)
    results = [book for book in books if query.lower() in book.lower() or query.lower() in books_details[book][2].lower()]
    
    if results:
        for result in results:
            results_list.insert(tk.END, result)
    else:
        messagebox.showinfo("تنبيه", "لا توجد نتائج مطابقة للبحث.")

# دالة لاستعارة كتاب
def borrow_book():
    selected_book = books_list.get(tk.ACTIVE)
    borrower_name = borrower_entry.get().strip()
    
    if not selected_book:
        messagebox.showerror("خطأ", "الرجاء اختيار كتاب من القائمة!")
        return
    if not borrower_name:
        messagebox.showerror("خطأ", "يرجى إدخال اسم المستعير!")
        return
    if selected_book in borrowed_books:
        messagebox.showerror("خطأ", f"الكتاب {selected_book} مستعار بالفعل!")
        return
    
    borrowed_books[selected_book] = borrower_name
    books.remove(selected_book)
    display_books()
    display_borrowed_books()
    messagebox.showinfo("نجاح", f"تم استعارة الكتاب: {selected_book} للمستعير: {borrower_name}.")

# دالة لعرض تقرير المكتبة
def show_report():
    total_books = len(books)
    borrowed_count = len(borrowed_books)
    messagebox.showinfo(
        "تقرير المكتبة",
        f"إجمالي الكتب المتوفرة: {total_books}\nإجمالي الكتب المستعارة: {borrowed_count}"
    )

# دالة لعرض قائمة الكتب
def display_books():
    books_list.delete(0, tk.END)
    for book in books:
        books_list.insert(tk.END, book)

# دالة لعرض قائمة الكتب المستعارة
def display_borrowed_books():
    borrowed_books_list.delete(0, tk.END)
    for book, borrower in borrowed_books.items():
        borrowed_books_list.insert(tk.END, f"{book} (مستعار من: {borrower})")

# دالة لتفريغ الحقول
def clear_entries():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    borrower_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)
    results_list.delete(0, tk.END)

# إنشاء واجهة المستخدم باستخدام Tkinter
root = tk.Tk()
root.title("نظام إدارة المكتبة")

# الإطار العلوي لإدخال البيانات
frame_top = tk.Frame(root, padx=10, pady=10)
frame_top.pack()

tk.Label(frame_top, text="عنوان الكتاب:").grid(row=0, column=0)
title_entry = tk.Entry(frame_top)
title_entry.grid(row=0, column=1)

tk.Label(frame_top, text="اسم المؤلف:").grid(row=1, column=0)
author_entry = tk.Entry(frame_top)
author_entry.grid(row=1, column=1)

tk.Label(frame_top, text="سنة النشر:").grid(row=2, column=0)
year_entry = tk.Entry(frame_top)
year_entry.grid(row=2, column=1)

tk.Label(frame_top, text="التصنيف:").grid(row=3, column=0)
category_entry = tk.Entry(frame_top)
category_entry.grid(row=3, column=1)

tk.Button(frame_top, text="إضافة كتاب", command=add_book).grid(row=4, column=0, columnspan=2, pady=10)

# الإطار الأوسط لعرض قائمة الكتب
frame_middle = tk.Frame(root, padx=10, pady=10)
frame_middle.pack()

tk.Label(frame_middle, text="قائمة الكتب:").pack()
books_list = tk.Listbox(frame_middle, width=50, height=10)
books_list.pack()

# البحث عن كتاب
frame_search = tk.Frame(root, padx=10, pady=10)
frame_search.pack()

tk.Label(frame_search, text="بحث عن كتاب (اسم/تصنيف):").grid(row=0, column=0)
search_entry = tk.Entry(frame_search)
search_entry.grid(row=0, column=1)

tk.Button(frame_search, text="بحث", command=search_books).grid(row=0, column=2)

tk.Label(frame_search, text="النتائج:").grid(row=1, column=0, columnspan=3)
results_list = tk.Listbox(frame_search, width=50, height=5)
results_list.grid(row=2, column=0, columnspan=3)

# استعارة كتاب
frame_borrow = tk.Frame(root, padx=10, pady=10)
frame_borrow.pack()

tk.Label(frame_borrow, text="اسم المستعير:").grid(row=0, column=0)
borrower_entry = tk.Entry(frame_borrow)
borrower_entry.grid(row=0, column=1)

tk.Button(frame_borrow, text="استعارة كتاب", command=borrow_book).grid(row=0, column=2)

# الإطار لعرض الكتب المستعارة
frame_borrowed = tk.Frame(root, padx=10, pady=10)
frame_borrowed.pack()

tk.Label(frame_borrowed, text="الكتب المستعارة:").pack()
borrowed_books_list = tk.Listbox(frame_borrowed, width=50, height=10)
borrowed_books_list.pack()

# عرض التقرير
frame_report = tk.Frame(root, padx=10, pady=10)
frame_report.pack()

tk.Button(frame_report, text="عرض تقرير المكتبة", command=show_report).pack()

# تشغيل الواجهة
root.mainloop()
