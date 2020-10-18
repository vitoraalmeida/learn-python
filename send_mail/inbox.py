# capaz de abrir mensagens de email
import imaplib
import email

host = 'imap.gmail.com'
username = 'dev.testm4il@gmail.com'
password = 'test@1234'

def get_inbox():
    #IMAP4_SSL é sublasse de IMAP4.
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    #search(charset, creterion[,...])
    #retorna lista com bytes referentes ao indice de cada email não lido
    _, search_data = mail.search(None, 'UNSEEN')

    my_message = []

    for num in search_data[0].split():
        email_data = {}
        #RFC822 = padrão para formato de arpa internet text messages
        # fetch retorna ( status, mensagem)
        # mensagem é uma lista de tuplas contendo um byte com o fomato(RFC822) e os
        # bytes da mensagem (cebeçalhos + corpo do email)
        _, data = mail.fetch(num, '(RFC822)')
        # seleciona o primeiro da lista que é o que contém a mensgem de fato
        _, msg_bytes = data[0]
        # faz o parsing da mensagem em bytes para o objeto Message
        email_message = email.message_from_bytes(msg_bytes)
        # mostra cada parte do cabeçalho
        for header in ['subject', 'to', 'from', 'date']:
            print(f"{header}: {email_message[header]}")
            email_data[header] = email_message[header]
        # percorre a mensagem, olhando os cabeçalhos, até achar o texto do corpo do email
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                # decode para converter de bytes para texto
                email_data['body'] = body.decode()
                print(email_data['body'])
                print('\n')
            if part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                # decode para converter de bytes para texto
                email_data['html_body'] = html_body.decode()
                print(email_data['html_body'])
                print('\n')

        my_message.append(email_data)
        return my_message


if __name__ == "__main__":
    my_inbox = get_inbox()
    print(my_inbox)

