from pika import ConnectionParameters, BlockingConnection

connection_params = ConnectionParameters(
    host="localhost",
    port=5672,
)

def process_message(ch, method, properties, body):
    print(f"Receiving a message: {body.decode()}")
    # 1/0 плохой способ auto_ack т.к. сообщение не отправится из-за ошибки (не дойдет)

    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    with BlockingConnection(connection_params) as conn:
        with conn.channel() as ch:
            ch.queue_declare(queue="messages")

            ch.basic_consume(
                queue="messages",
                on_message_callback=process_message,
                # auto_ack=True, # подтверждение получения сообщения и удаление
            )
            print("Wait messages")
            ch.start_consuming()


if __name__ == "__main__":
    main()