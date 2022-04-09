from kombu import Exchange, Queue

from classic.messaging_kombu import BrokerScheme


broker_scheme = BrokerScheme(
    Queue("IssueQ", Exchange("ApiEx"), routing_key="issue", max_length=10)
)
