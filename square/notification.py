from notifications.signals import notify


def send_notifications(actor, verb, recipient, target=None, description=None, **kwargs):

    notify.send(sender=actor,
                recipient=recipient,
                verb=verb,
                target=target,
                description=description,
                **kwargs)
