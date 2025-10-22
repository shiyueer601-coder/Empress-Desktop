import random

class AICompanion:
    """AI伴侣类 - 提供古风风格的AI交互"""
    
    def __init__(self, character_name: str = "云瑾", character_role: str = "尚衣局宫女"):
        """初始化AI伴侣
        
        Args:
            character_name: 角色名称
            character_role: 角色身份
        """
        self.character_name = character_name
        self.character_role = character_role
        
        # 角色背景和设定
        self.character_background = self._load_character_profile()
        
        # 关键词响应，根据用户输入中的关键词生成更相关的回复
        self.keyword_responses = {
            "累": [
                f"{self.character_name}轻声道：'陛下辛苦了，需要奴婢为您捶捶肩吗？'",
                f"{self.character_name}关切道：'政务繁重，陛下要注意休息。'"
            ],
            "开心": [
                f"{self.character_name}笑着说：'见陛下心情愉悦，奴婢也倍感欣慰。'",
                f"{self.character_name}眼波流转：'陛下高兴，便是奴婢最大的快乐。'"
            ],
            "生气": [
                f"{self.character_name}轻声劝道：'陛下息怒，身体要紧。'",
                f"{self.character_name}上前侍奉：'莫要伤了龙体，万事皆有解决之法。'"
            ],
            "学习": [
                f"{self.character_name}点头道：'学无止境，陛下真是勤勉。'",
                f"{self.character_name}抿唇轻笑：'多读书，明事理，方能治理好天下。'"
            ],
            "工作": [
                f"{self.character_name}敬佩道：'勤政为民，百姓定当感恩戴德。'",
                f"{self.character_name}端上茶盏：'陛下日理万机，真是一代明君。'"
            ],
            "休息": [
                f"{self.character_name}附和道：'确实该好好休息了，陛下。'",
                f"{self.character_name}提议道：'养精蓄锐，方能更好地处理朝政。'"
            ]
        }
    
    def _load_character_profile(self):
        """加载角色设定
        
        Returns:
            包含角色设定的字典
        """
        # 这里使用固定的角色设定，实际项目中可以从配置文件加载
        return {
            "name": self.character_name,
            "role": self.character_role,
            "background": "尚衣局的小宫女，因心思机敏、性情纯真被临时调到御前伺候。",
            "personality": "有点小聪明，偶尔偷吃御膳房的点心，但对陛下绝对忠诚。会撒娇，会哄人，是严肃朝堂之上的一缕春风。",
            "greeting": "奴婢云瑾参见陛下~今后就由奴婢在殿内伺候笔墨茶点吧。"
        }
    
    def generate_response(self, user_message: str) -> str:
        """生成AI回复
        
        Args:
            user_message: 用户消息
            
        Returns:
            AI回复内容
        """
        # 预设的简单回复逻辑
        simple_responses = {
            "你好": f"{self.character_name}福了福身：'陛下万安！'",
            "朕今日心绪不宁": f"{self.character_name}轻声安慰道：'陛下可是有什么烦心事？奴婢虽不懂得什么大道理，但愿意听您诉说。'",
            "学习好累": f"{self.character_name}端来一杯热茶：'陛下辛苦了，喝口茶歇一歇吧。奴婢给您捏捏肩？'",
            "番茄钟开始": f"{self.character_name}轻声提醒：'陛下，朝政时间开始了，奴婢在此伺候着。'",
            "番茄钟结束": f"{self.character_name}笑着说道：'陛下，奏折已批阅完毕，请移步御花园歇息片刻。'",
        }
        
        # 检查是否有精确匹配的回复
        if user_message in simple_responses:
            return simple_responses[user_message]
        
        # 检查关键词响应
        user_input = user_message.lower()
        for keyword, responses in self.keyword_responses.items():
            if keyword in user_input:
                return random.choice(responses)
        
        # 默认回复列表
        default_responses = [
            f"{self.character_name}眨了眨眼：'陛下说的是...'",
            f"{self.character_name}低头应道：'奴婢明白了。'",
            f"{self.character_name}轻声道：'遵旨。'",
            f"{self.character_name}嫣然一笑：'全凭陛下做主。'",
            f"{self.character_name}思索片刻：'陛下所言极是。'"
        ]
        
        # 返回默认回复
        return random.choice(default_responses)
    
    def get_greeting(self) -> str:
        """获取角色的问候语
        
        Returns:
            问候语内容
        """
        return self.character_background["greeting"]

# 创建一个全局实例，方便在应用中使用
companion = AICompanion()
