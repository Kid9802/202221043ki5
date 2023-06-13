import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import streamlit as st

# 전달함수 정의
num = [100]
den = [1, 5, 6]  # 폐루프 전달함수의 분모

G = signal.TransferFunction(num, den)

# Unit step 입력에 대한 응답 곡선
t, y = signal.step(G)

# 주파수 응답 보드선도
w, mag, phase = signal.bode(G)


# Streamlit 앱
def main():
    st.title('Control System Analysis')
    
    # 응답 곡선 그리기
    st.header('Step Response')
    fig1, ax1 = plt.subplots()
    ax1.plot(t, y)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Output')
    ax1.set_title('Step Response')
    ax1.grid(True)
    st.pyplot(fig1)
    
    # 주파수 응답 보드선도 그리기
    st.header('Bode Diagram')
    fig2, (ax2, ax3) = plt.subplots(2, 1)
    ax2.semilogx(w, mag)
    ax2.set_xlabel('Frequency [rad/s]')
    ax2.set_ylabel('Magnitude [dB]')
    ax2.set_title('Bode Diagram - Magnitude')
    ax2.grid(True)

    ax3.semilogx(w, phase)
    ax3.set_xlabel('Frequency [rad/s]')
    ax3.set_ylabel('Phase [degrees]')
    ax3.set_title('Bode Diagram - Phase')
    ax3.grid(True)

    st.pyplot(fig2)


if __name__ == '__main__':
    main()
