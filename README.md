
# pdfsplit

A simple CLI tool to quickly split PDF files or eBooks into multiple chapter subfiles without the hassle of “print to PDF.”

---

## Features

- Splits PDFs based on defined chapter start pages.
- Optionally skips pages at the beginning of the document (offset).
- Saves individual chapters in a new folder named after the original PDF.

---

## Installation

```bash
/bin/python3 -m pip install git+https://github.com/kamexx/pdf_splitter.git@main
```

---

## Usage

1. Change to the directory where your PDF file is located:
   ```bash
   cd /path/to/pdf
   ```

2. Run the script with the required parameters:
   ```bash
   /bin/python3 -m pdfsplit.pdfsplit --filename "filename.pdf" --offset 0 --chapter 1 10 20 30
   ```

### Parameters

- `--filename`: Name of the PDF file (including extension).
- `--offset`: Number of pages to skip at the beginning (default: 0).
- `--chapter`: List of page numbers where each chapter starts.

---

## Example

```bash
cd my_pdf_collection/
  
/bin/python3 -m pdfsplit.pdfsplit --filename myscript.pdf --offset 18 --chapter 1 9 35 53 71 93 117 127 139 153 169
```

The script will create a new folder called `myscript` and save the individual chapters as separate PDF files there.

---

## Optional

You can also add the Python package to your `PATH` to run the tool without using the full command `/bin/python3 -m pdfsplit.pdfsplit`.

---

## License

MIT License  
(C) 2025 by kamexx

---

Feel free to reach out if you have any questions or issues!
