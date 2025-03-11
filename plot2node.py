import matplotlib.pyplot as plt

# Dữ liệu số lượng nút, Throughput và PDR
nodes = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
throughput = [0.842628, 0.842628, 0.842628, 0.842628, 0.84262, 0.842628, 0.842628, 
              0.842628, 0.84262, 0.84262, 0.84262, 0.842607, 0.815222, 0.739388, 0.0]
pdr = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 96.75, 87.75, 0]

# Tạo biểu đồ
fig, ax1 = plt.subplots(figsize=(8, 5))

# Trục Y đầu tiên (Throughput)
ax1.set_xlabel("Số lượng nút")
ax1.set_ylabel("Throughput (Mbps)", color='tab:blue')
ax1.plot(nodes, throughput, marker='o', linestyle='-', color='tab:blue', label="Throughput")
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Trục Y thứ hai (PDR)
ax2 = ax1.twinx()
ax2.set_ylabel("PDR (%)", color='tab:red')
ax2.plot(nodes, pdr, marker='s', linestyle='--', color='tab:red', label="PDR")
ax2.tick_params(axis='y', labelcolor='tab:red')

# Tiêu đề và lưới
plt.title("Hiệu suất mạng CSMA/CA khi tăng số lượng nút")
ax1.grid(True, linestyle='--', alpha=0.6)

# Hiển thị biểu đồ
plt.show()
