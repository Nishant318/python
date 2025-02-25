def convert_bytes(byte_size):
    KB = 1024
    MB = KB * 1024
    GB = MB * 1024
    kb = byte_size / KB
    mb = byte_size / MB
    gb = byte_size / GB

    return kb, mb, gb

byte_size = int(input("Enter the size in bytes: "))
kb, mb, gb = convert_bytes(byte_size)

print(f"{byte_size} bytes is equal to:")
print(f"{kb} KB")
print(f"{mb} MB")
print(f"{gb} GB")
