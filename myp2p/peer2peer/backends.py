import smtplib
from django.core.mail.backends.smtp import EmailBackend
from django.utils.encoding import force_bytes

class UnverifiedEmailBackend(EmailBackend):
    def open(self, *args, **kwargs):
        if not self.connection:
            self.connection = smtplib.SMTP(self.host, self.port)
            self.connection.starttls()
            self.connection.sock = smtplib.ssl.wrap_socket(
                self.connection.sock,
                cert_reqs=smtplib.ssl.CERT_NONE,
                ssl_version=smtplib.ssl.PROTOCOL_TLS
            )
        return super().open(*args, **kwargs)

    def send_messages(self, email_messages):
        if not email_messages:
            return 0
        num_sent = 0
        for message in email_messages:
            num_sent += message.send(fail_silently=True)
        return num_sent
