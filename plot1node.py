import matplotlib.pyplot as plt

# Dữ liệu từ mô phỏng
nodes = list(range(2, 31))
throughput = [
    0.842628, 0.842628, 0.84262, 0.84262, 0.842628, 0.842628, 0.842628, 0.842628, 0.842607, 
    0.842628, 0.842628, 0.842628, 0.84262, 0.84262, 0.842628, 0.842628, 0.842628, 0.84262, 
    0.842607, 0.842626, 0.84262, 0.842607, 0.84262, -0, 0.84262, 0.424529, 0.842607, -0, -0
]
pdr = [
    100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 
    100, 100, 100, 100, 100, 0, 100, 42.375, 100, 0, 0
]

# Vẽ biểu đồ
fig, ax1 = plt.subplots(figsize=(10, 5))

# Trục Y bên trái - Throughput
ax1.set_xlabel("Number of Nodes")
ax1.set_ylabel("Throughput (Mbps)", color="tab:blue")
ax1.plot(nodes, throughput, marker="o", linestyle="-", color="tab:blue", label="Throughput")
ax1.tick_params(axis="y", labelcolor="tab:blue")

# Trục Y bên phải - PDR
ax2 = ax1.twinx()
ax2.set_ylabel("PDR (%)", color="tab:red")
ax2.plot(nodes, pdr, marker="s", linestyle="--", color="tab:red", label="PDR")
ax2.tick_params(axis="y", labelcolor="tab:red")

# Tiêu đề và hiển thị
plt.title("Network Performance Analysis (Throughput & PDR vs. Number of Nodes)")
fig.tight_layout()
plt.show()
