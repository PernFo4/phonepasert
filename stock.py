import socket

def handle_client_connection(client_socket):
    """
    Hàm xử lý kết nối từ client.
    """
    try:
        while True:
            # Nhận dữ liệu từ client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break  # Ngắt kết nối nếu không nhận được dữ liệu

            print(f"Nhận được: {data}")

            # Giả sử dữ liệu cần tách stroke là văn bản
            response = process_stock_protocol(data)

            # Gửi lại kết quả cho client
            client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Lỗi xử lý kết nối: {e}")
    finally:
        client_socket.close()

def process_stock_protocol(data):
    """
    Xử lý giao thức STOCK.
    Tách stroke (giả sử stroke là ký tự cách) và trả về kết quả.
    """
    try:
        # Tách dữ liệu thành các phần tử dựa trên khoảng trắng
        words = data.strip().split()
        return " | ".join(words)  # Kết quả trả về, tách bằng " | "
    except Exception as e:
        return f"Lỗi xử lý giao thức: {e}"

def start_server(host='0.0.0.0', port=99):
    """
    Khởi động server tại host và port được chỉ định.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server đang chạy trên {host}:{port}...")

    try:
        while True:
            # Chờ kết nối từ client
            client_socket, addr = server_socket.accept()
            print(f"Kết nối từ {addr}")
            handle_client_connection(client_socket)
    except KeyboardInterrupt:
        print("\nServer đã dừng.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
    
