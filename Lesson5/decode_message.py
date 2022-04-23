from struct import *

packet = b'\x08\x00\x00\x00\xf6\x01\x00\x00\x24\x00\x00\x00\x03\x00\x00\x00\x0c\x00\x00\x00I think, therefore I am.\xca\xcd\x00\x00'

#### Don't change the code until this line ####


def show_details():
    # print sender ID (decimal), message ID (decimal), the actual message (readable english text), and its checksum (decimal)
    sender_id, receiver_id, content_size, session_id, message_id = unpack(
        "<IIIII", packet[:20])
    content, = unpack(f'<{content_size-12}s', packet[20:-4])
    checksum, = unpack("<I", packet[-4:])
    print(f"Sender ID: {sender_id}")
    print(f"Message ID: {message_id}")
    print(f"Message Text: {content.decode('UTF-8')}")
    print(f"Checksum: {checksum}")


show_details()
