import cry
import sys

try:
    # .so ဖိုင်ထဲက main function ကို တိုက်ရိုက်ခေါ်လိုက်တာပါ
    cry.main()
except KeyboardInterrupt:
    print("\n[!] ပိတ်လိုက်ပါပြီ။")
    sys.exit()
except Exception as e:
    print(f"\n[!] Error တစ်ခုတက်နေပါတယ်: {e}")
  
