import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font

# Vibrant orange-pink color scheme
COLORS = {
    'primary': '#FF6B6B',      # Coral pink
    'secondary': '#FF9A76',    # Peach orange
    'success': '#4ECDC4',      # Turquoise
    'error': '#FF4081',        # Hot pink
    'background': '#FFF9F5',   # Soft cream
    'text': '#FF4858',         # Bright coral
    'button_hover': '#FFB2B2'  # Light pink
}

def reverse_number(n: int) -> int:
    """Return the reverse of an integer."""
    reversed_num = 0
    original = abs(n)
    while original > 0:
        reversed_num = (reversed_num * 10) + (original % 10)
        original //= 10
    return reversed_num if n >= 0 else -reversed_num


def is_palindrome(n: int) -> bool:
    """Return True if n is a palindrome."""
    return n == reverse_number(n)


class NumberToolsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔢 Number Tools")
        self.root.geometry("400x500")
        self.root.configure(padx=20, pady=20)

        # Style configuration
        style = ttk.Style()
        style.configure("Title.TLabel", font=("Arial", 24, "bold"))
        style.configure("Result.TLabel", font=("Arial", 16))
        style.configure("TButton", font=("Arial", 12))
        style.configure("TEntry", font=("Arial", 12))

        # Title
        self.title_label = tk.Label(
            root, 
            text="Number Tools",
            font=('Arial', 28, 'bold'),
            fg=COLORS['text'],
            bg=COLORS['background']
        )
        self.title_label.pack(pady=20)

        # Input frame
        input_frame = tk.Frame(root, bg=COLORS['background'])
        input_frame.pack(fill="x", pady=20)

        self.input_label = tk.Label(
            input_frame, 
            text="Enter a number:",
            font=('Arial', 14),
            fg=COLORS['text'],
            bg=COLORS['background']
        )
        self.input_label.pack()

        self.number_entry = tk.Entry(
            input_frame,
            width=20,
            font=('Arial', 14),
            bg='white',
            fg=COLORS['text'],
            insertbackground=COLORS['primary'],
            relief='flat',
            justify='center'
        )
        self.number_entry.pack(pady=10)

        # Add a decorative line under the entry
        entry_underline = tk.Frame(
            input_frame,
            height=2,
            bg=COLORS['primary']
        )
        entry_underline.pack(fill='x', padx=50)

        # Buttons frame
        button_frame = tk.Frame(root, bg=COLORS['background'])
        button_frame.pack(fill="x", pady=20)

        # Create styled buttons
        self.reverse_button = tk.Button(
            button_frame,
            text="🔄 Reverse Number",
            command=self.reverse_number,
            bg=COLORS['primary'],
            fg='white',
            activebackground=COLORS['button_hover'],
            activeforeground='white',
            font=('Arial', 12, 'bold'),
            relief='flat',
            borderwidth=0,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        self.reverse_button.pack(pady=5, fill="x")
        self.reverse_button.bind('<Enter>', lambda e: self.reverse_button.config(bg=COLORS['button_hover']))
        self.reverse_button.bind('<Leave>', lambda e: self.reverse_button.config(bg=COLORS['primary']))

        self.check_palindrome_button = tk.Button(
            button_frame,
            text="🔍 Check Palindrome",
            command=self.check_palindrome,
            bg=COLORS['primary'],
            fg='white',
            activebackground=COLORS['button_hover'],
            activeforeground='white',
            font=('Arial', 12, 'bold'),
            relief='flat',
            borderwidth=0,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        self.check_palindrome_button.pack(pady=5, fill="x")
        self.check_palindrome_button.bind('<Enter>', lambda e: self.check_palindrome_button.config(bg=COLORS['button_hover']))
        self.check_palindrome_button.bind('<Leave>', lambda e: self.check_palindrome_button.config(bg=COLORS['primary']))

        # Results frame
        results_frame = tk.Frame(root, bg=COLORS['background'])
        results_frame.pack(fill="x", pady=20)

        self.result_label = tk.Label(
            results_frame, 
            text="",
            font=('Arial', 16, 'bold'),
            fg=COLORS['primary'],
            bg=COLORS['background'],
            wraplength=350
        )
        self.result_label.pack(pady=10)

    def create_custom_styles(self):
        """Create custom styles for widgets"""
        self.root.option_add('*TButton*Padding', 20)

    def get_input_number(self) -> int:
        """Get and validate input number"""
        try:
            return int(self.number_entry.get())
        except ValueError:
            messagebox.showerror("Error", "⚠️ Please enter a valid integer!")
            return None

    def reverse_number(self):
        """Handle reverse number button click"""
        num = self.get_input_number()
        if num is not None:
            result = reverse_number(num)
            self.result_label.config(
                text=f"🔄 Reversed number: {result}",
                fg=COLORS['secondary'])

    def check_palindrome(self):
        """Handle check palindrome button click"""
        num = self.get_input_number()
        if num is not None:
            if is_palindrome(num):
                self.result_label.config(
                    text=f"✅ {num} is a palindrome!",
                    fg=COLORS['success']
                )
            else:
                self.result_label.config(
                    text=f"❌ {num} is not a palindrome.",
                    fg=COLORS['error']
                )


def main():
    root = tk.Tk()
    app = NumberToolsApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
