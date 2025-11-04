# 填入你自己的api_key。在https://deepseek.nwafu.edu.cn里面找，具体看教程
API_KEY = "sk-8baa5***********"

API_URL_REDIRECT = {"https://api.openai.com/v1/chat/completions": "https://deepseek.nwafu.edu.cn/api/chat/completions"}

NWAFU_COOKIE = "__Secure-Login-State-cas=自己填入"

# live2d装饰（左下角小人），填入False关闭。
ADD_WAIFU = True

DARK_MODE = False

THEME = "Chuanhu-Small-and-Beautiful"

LLM_MODEL = "one-api-Qwen3-235B-A22B" # 可选 ↓↓↓
AVAIL_LLM_MODELS = ["one-api-Qwen3-235B-A22B", "one-api-Qwen3-235B-A22B", "one-api-Qwen3-32B", 
                    "one-api-qwen3-235b-a22b-nothink", "one-api-Qwen3-VL-235B-A22B-Instruct"
                    ]

# 字体修改，如果，替换方法，将"Theme-Default-Font"替换成下面的就行
FONT = "Theme-Default-Font"
AVAIL_FONTS = [
    "默认值(Theme-Default-Font)", 
    "宋体(SimSun)",  
    "黑体(SimHei)",  
    "楷体(KaiTi)",  
    "仿宋(FangSong)",  
    "华文细黑(STHeiti Light)",
    "华文楷体(STKaiti)",  
    "华文仿宋(STFangsong)",  
    "华文宋体(STSong)",  
    "华文中宋(STZhongsong)",  
    "华文新魏(STXinwei)",  
    "华文隶书(STLiti)", 
    # 备注：以下字体需要网络支持，您可以自定义任意您喜欢的字体，如下所示，需要满足的格式为 "字体昵称(字体英文真名@字体css下载链接)" 
    "思源宋体(Source Han Serif CN VF@https://chinese-fonts-cdn.deno.dev/packages/syst/dist/SourceHanSerifCN/result.css)",
    "月星楷(Moon Stars Kai HW@https://chinese-fonts-cdn.deno.dev/packages/moon-stars-kai/dist/MoonStarsKaiHW-Regular/result.css)",
    "珠圆体(MaokenZhuyuanTi@https://chinese-fonts-cdn.deno.dev/packages/mkzyt/dist/猫啃珠圆体/result.css)",
    "平方萌萌哒(PING FANG MENG MNEG DA@https://chinese-fonts-cdn.deno.dev/packages/pfmmd/dist/平方萌萌哒/result.css)"
]