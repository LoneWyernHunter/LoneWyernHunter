def sendEmail(correo):

    sender_email = 'xiangqips@gmail.com'
    email_password = 'Xiangqi2022'

    #contacts = ['741278@unizar.es', 'test@example.com']

    msg = EmailMessage()
    msg['Subject'] = 'Comprobación de cuenta de usuario'
    msg['From'] = sender_email
    msg['To'] = correo

    msg.set_content('Comprobación de la cuenta de usuario')

    msg.add_alternative("""\
        <html>
            <body>
                <p><b>Validación de la cuenta de usuario</b>
                    Haz click en el enlace <a href="www.google.es">Validar Cuenta</a> 
                    para validar tu cuenta de usuario.
            <   /p>
            </body>
        </html>
    """, subtype='html')


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, email_password)
        smtp.send_message(msg)