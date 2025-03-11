include \masm32\include\massm32rt.inc
section .data
    msg db "Hello, World!", 0  ; Chuỗi ký tự kết thúc bằng NULL

section .text
    global main
    extern printf  ; Gọi hàm printf từ thư viện C

main:
    sub rsp, 40    ; Căn chỉnh stack cho Windows ABI (cần chia hết cho 16)
    lea rcx, [msg] ; Đưa địa chỉ msg vào RCX (tham số thứ nhất của printf)
    call printf    ; Gọi hàm printf
    add rsp, 40    ; Phục hồi stack
    ret            ; Trả về
