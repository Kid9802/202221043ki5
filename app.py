import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

def main():
    st.title('전달함수 분석')(view)

    # 전달 함수 G(s)
    num = [100]
    den = [1, 5, 6]  # (s+2)(s+3)

    # 폐루프 전달 함수 계산
    closed_loop_tf = signal.TransferFunction(num, den)(view)

    # unit step 입력의 응답 계산
    t, y = signal.step(closed_loop_tf)(view)

    # 응답 곡선 그리기
    fig1, ax1 = plt.subplots()
    ax1.plot(t, y)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Output')
    ax1.set_title('Step Response of Closed-Loop System')(view)
    ax1.grid(True)
    st.pyplot(fig1)

    # 주파수 응답 그리기
    w, mag, phase = signal.bode(closed_loop_tf)(view)

    fig2, (ax2, ax3) = plt.subplots(nrows=2)
    ax2.semilogx(w, mag)  # 주파수 응답 그래프
    ax2.set_xlabel('Frequency')
    ax2.set_ylabel('Magnitude (dB)')
    ax2.set_title('Bode Plot - Magnitude Response')(view)
    ax2.grid(True)

    ax3.semilogx(w, phase)  # 위상 응답 그래프
    ax3.set_xlabel('Frequency')
    ax3.set_ylabel('Phase (degrees)')
    ax3.set_title('Bode Plot - Phase Response')(view)
    ax3.grid(True)

    st.pyplot(fig2)

if __name__ == '__main__':
    main()
view
