import math

# ==========================================
# 1. 共通の数値を記入
# ==========================================
alpha = 1.42     #センサ感度による定数
D  = -4.3879     #定数
A = 0.000002043  #定数
B = 0.0000775    #定数
C = 68048730     #定数
C2 = 0.014388    #定数
K = 273.15       #絶対値換算値
T = 40           #金型温度

# ==========================================
# 2.メインの計算処理
# ==========================================
#上から順番に計算を行う。execute_main_calc(data_Vom, data_Vos)
def execute_main_calc(data_Vom, data_Vos):
   
   #Va の計算 
   try:
       # 分母: A(T + K) + B
       denominator = A * (T + K) + B
         
       # 数式: V = C * exp(-D / 分母)
       Va = C * math.exp(-C2 / denominator)

   except ZeroDivisionError:
        print("エラー: 分母が0になったため計算できません。A, B, T, E の値を確認してください。")
   
   #Voe = exp(Vom) + D を計算する関数

   Vome = math.exp(data_Vom) + D

   #Vose = exp(Vos) + D を計算する関数
   Vose = math.exp(data_Vos) + D

   #Vcomp_se の計算
   Vcomp_se = alpha * Vose

   #Vcomp_se の計算 
   Vcomp_me = alpha * Vome

   #Vdivの計算
   Vdiv = Va - Vcomp_se

   #温度(℃)の計算 
   ln_C = math.log(C)

   ln_Vcomp_Vdiv = math.log(Vcomp_me + Vdiv)

   T_k = (C2/A) / (ln_C - ln_Vcomp_Vdiv) - B/A
    # 算出した温度をセルシウス温度に変換
   T_celsius = T_k - K
    
   return T_celsius
