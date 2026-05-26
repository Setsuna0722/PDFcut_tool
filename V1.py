import os
from tkinter import (
    Tk, filedialog, messagebox, Toplevel,
    Label, StringVar, Button, Radiobutton, IntVar, simpledialog
)
from tkinter.ttk import Progressbar
from PyPDF2 import PdfReader, PdfWriter


# ---------- 工具函數 ----------
def parse_page_range(page_input, total_pages):
    pages = set()
    for part in page_input.split(','):
        part = part.strip()
        if '-' in part:
            try:
                start, end = map(int, part.split('-'))
                pages.update(range(start - 1, end))
            except:
                continue
        else:
            try:
                pages.add(int(part) - 1)
            except:
                continue
    return sorted(p for p in pages if 0 <= p < total_pages)


def is_blank_page(page):
    text = page.extract_text()
    return not text or text.strip() == ""


def update_progress(index, total, progress_bar):
    progress_bar['value'] = (index / total) * 100
    progress_bar.update_idletasks()


def show_progress_window():
    progress_window = Toplevel()
    progress_window.title("處理進度")

    status_var = StringVar()
    status_var.set("準備中...")

    status_label = Label(progress_window, textvariable=status_var)
    status_label.pack(pady=10)

    progress_bar = Progressbar(progress_window, orient="horizontal", length=300, mode="determinate")
    progress_bar.pack(pady=20)

    return progress_window, progress_bar, status_var.set


# ---------- 模式 A ----------
def split_all_pages(pdf_paths, progress_callback, status_callback):
    for index, pdf_path in enumerate(pdf_paths, start=1):
        try:
            filename = os.path.basename(pdf_path)
            folder_name = os.path.splitext(filename)[0]
            output_folder = os.path.join(os.path.dirname(pdf_path), folder_name)

            os.makedirs(output_folder, exist_ok=True)

            reader = PdfReader(pdf_path)
            total_pages = len(reader.pages)

            for i in range(total_pages):
                writer = PdfWriter()
                writer.add_page(reader.pages[i])
                output_path = os.path.join(output_folder, f"{folder_name}_page_{i + 1}.pdf")
                with open(output_path, "wb") as f:
                    writer.write(f)

            status_callback(f"✅ 分割完成：{filename} → {total_pages} 頁")
        except Exception as e:
            status_callback(f"❌ 分割失敗：{filename}，錯誤：{e}")

        progress_callback(index, len(pdf_paths))

    messagebox.showinfo("完成", "所有檔案已成功分割完畢！")


# ---------- 模式 B ----------
def split_selected_pages(pdf_path, progress_callback, status_callback):
    try:
        reader = PdfReader(pdf_path)
        total_pages = len(reader.pages)

        page_input = simpledialog.askstring("輸入頁碼", "請輸入要分割的頁碼（例如：1,3-5）：")
        if not page_input:
            return

        page_numbers = parse_page_range(page_input, total_pages)
        if not page_numbers:
            status_callback("❌ 沒有有效頁碼")
            return

        remove_blank = messagebox.askyesno("排除空白頁", "是否排除空白頁？")

        writer = PdfWriter()
        skipped_blank = 0
        for p in page_numbers:
            page = reader.pages[p]
            if remove_blank and is_blank_page(page):
                skipped_blank += 1
                status_callback(f"⚠️ 已略過空白頁：第 {p + 1} 頁")
                continue
            writer.add_page(page)

        if not writer.pages:
            status_callback("❌ 分割失敗：所有頁面皆為空白或無效")
            return

        output_name = os.path.splitext(os.path.basename(pdf_path))[0] + "_selected_pages.pdf"
        output_path = os.path.join(os.path.dirname(pdf_path), output_name)

        with open(output_path, "wb") as f:
            writer.write(f)

        status_callback(f"✅ 分割完成：{output_name}（略過空白頁 {skipped_blank} 頁）")
        messagebox.showinfo("完成", f"已成功分割頁面為：{output_name}")

    except Exception as e:
        status_callback(f"❌ 錯誤：{e}")

    progress_callback(1, 1)


# ---------- 模式選擇 ----------
def choose_mode(callback):
    def submit():
        selected_mode = mode.get()
        select_window.destroy()
        callback(selected_mode)

    select_window = Tk()
    select_window.title("選擇分割模式")

    Label(select_window, text="請選擇分割方式：").pack(pady=10)
    mode = IntVar()
    mode.set(1)

    Radiobutton(select_window, text="模式 A：分割所有頁面（可多選 PDF）", variable=mode, value=1).pack(anchor="w", padx=20)
    Radiobutton(select_window, text="模式 B：分割特定頁面（單一 PDF）", variable=mode, value=2).pack(anchor="w", padx=20)

    Button(select_window, text="確定", command=submit).pack(pady=10)

    select_window.mainloop()


# ---------- 主程式 ----------
def main():
    def run_with_mode(selected_mode):
        root = Tk()
        root.withdraw()

        if selected_mode == 1:
            pdf_files = filedialog.askopenfilenames(
                title="選擇要分割的 PDF（可多選）",
                filetypes=[("PDF Files", "*.pdf")]
            )
            if pdf_files:
                progress_window, progress_bar, set_status = show_progress_window()
                split_all_pages(pdf_files, lambda i, t: update_progress(i, t, progress_bar), set_status)
                progress_window.destroy()

        elif selected_mode == 2:
            pdf_file = filedialog.askopenfilename(
                title="選擇要分割的 PDF",
                filetypes=[("PDF Files", "*.pdf")]
            )
            if pdf_file:
                progress_window, progress_bar, set_status = show_progress_window()
                split_selected_pages(pdf_file, lambda i, t: update_progress(i, t, progress_bar), set_status)
                progress_window.destroy()
        root.destroy()

    choose_mode(run_with_mode)


if __name__ == "__main__":
    main()
