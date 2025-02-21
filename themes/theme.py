import pickle
import base64
import uuid
import json
from toolbox import get_conf
import json


"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
第 1 部分
加载主题相关的工具函数
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""


def load_dynamic_theme(THEME):
    adjust_dynamic_theme = None
    if THEME == "Chuanhu-Small-and-Beautiful":
        from .green import adjust_theme, advanced_css

        theme_declaration = (
            '<h3 align="center" class="small">本站由🎈一只爱跳水的兔子❤搭建，仅供学术使用。</h3>'
            '<h3 style="display: flex; justify-content: center; gap: 10px;">'
            '<a href="https://gpt.nwafu-ai.me" target="_blank" style="text-align: center; text-decoration: none;">🧪官网主页</a>'
            '<a href="http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=yfptzEImDm0f-cJY2WXF5mkT3Ak0BPHC&authKey=IxpiZlQvPeBeWCgFbLq5z92%2FhmkgqLS5oviMdJRdnoDIWqMRjQ8%2BAYEMKUHJeO3Y&noverify=0&group_code=923014731" target="_blank" style="text-align: center; text-decoration: none;">🔑反馈问题</a>'
            '<a href="https://blog.nwafu-ai.cn/archives/1705730973556" target="_blank" style="text-align: center; text-decoration: none;">📝查看教程</a>'
            '</h3>'
        )
    elif THEME == "High-Contrast":
        from .contrast import adjust_theme, advanced_css

        theme_declaration = ""
    elif "/" in THEME:
        from .gradios import adjust_theme, advanced_css
        from .gradios import dynamic_set_theme

        adjust_dynamic_theme = dynamic_set_theme(THEME)
        theme_declaration = ""
    else:
        from .default import adjust_theme, advanced_css

        theme_declaration = ""
    return adjust_theme, advanced_css, theme_declaration, adjust_dynamic_theme


adjust_theme, advanced_css, theme_declaration, _ = load_dynamic_theme(get_conf("THEME"))


"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
第 2 部分
cookie相关工具函数
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""
def assign_user_uuid(cookies):
    # 为每一位访问的用户赋予一个独一无二的uuid编码
    cookies.update({"uuid": uuid.uuid4()})
    return cookies


def to_cookie_str(d):
    # serialize the dictionary and encode it as a string
    serialized_dict = json.dumps(d)
    cookie_value = base64.b64encode(serialized_dict.encode('utf8')).decode("utf-8")
    return cookie_value


def from_cookie_str(c):
    # Decode the base64-encoded string and unserialize it into a dictionary
    serialized_dict = base64.b64decode(c.encode("utf-8"))
    serialized_dict.decode("utf-8")
    return json.loads(serialized_dict)


"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
第 3 部分
内嵌的javascript代码（这部分代码会逐渐移动到common.js中）
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

js_code_for_toggle_darkmode = """() => {
    if (document.querySelectorAll('.dark').length) {
        setCookie("js_darkmode_cookie", "False", 365);
        document.querySelectorAll('.dark').forEach(el => el.classList.remove('dark'));
    } else {
        setCookie("js_darkmode_cookie", "True", 365);
        document.querySelector('body').classList.add('dark');
    }
    document.querySelectorAll('code_pending_render').forEach(code => {code.remove();})
}"""


js_code_clear = """
(a,b)=>{
    return ["", ""];
}
"""


js_code_show_or_hide = """
(display_panel_arr)=>{
setTimeout(() => {
    // get conf
    display_panel_arr = get_checkbox_selected_items("cbs");

    ////////////////////// 输入清除键 ///////////////////////////
    let searchString = "输入清除键";
    let ele = "none";
    if (display_panel_arr.includes(searchString)) {
        let clearButton = document.getElementById("elem_clear");
        let clearButton2 = document.getElementById("elem_clear2");
        clearButton.style.display = "block";
        clearButton2.style.display = "block";
        setCookie("js_clearbtn_show_cookie", "True", 365);
    } else {
        let clearButton = document.getElementById("elem_clear");
        let clearButton2 = document.getElementById("elem_clear2");
        clearButton.style.display = "none";
        clearButton2.style.display = "none";
        setCookie("js_clearbtn_show_cookie", "False", 365);
    }

    ////////////////////// 基础功能区 ///////////////////////////
    searchString = "基础功能区";
    if (display_panel_arr.includes(searchString)) {
        ele = document.getElementById("basic-panel");
        ele.style.display = "block";
    } else {
        ele = document.getElementById("basic-panel");
        ele.style.display = "none";
    }

    ////////////////////// 函数插件区 ///////////////////////////
    searchString = "函数插件区";
    if (display_panel_arr.includes(searchString)) {
        ele = document.getElementById("plugin-panel");
        ele.style.display = "block";
    } else {
        ele = document.getElementById("plugin-panel");
        ele.style.display = "none";
    }

}, 50);
}
"""

