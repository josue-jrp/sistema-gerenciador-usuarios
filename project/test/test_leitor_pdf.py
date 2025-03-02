import PyPDF2

def leitor_pdf(x):
    with open(f"{x}.pdf", "rb")as arquivo:
        pdf_file = PyPDF2.PdfReader(arquivo)

        for i in range(len(pdf_file.pages)):
            pagina = pdf_file.pages[i]
            text = pagina.extract_text()
            print(text)

arquivo_pdf = input("Digite aqui o caminho para o arquivo: (sem extensão de arquivo)")

leitor_pdf(arquivo_pdf)
            
 