from typing import Any, List, Optional, Union
from pydantic import BaseModel, Field, root_validator, validator
from datetime import date

# --- Models ---

class CourseHours(BaseModel):
    total: int = Field(..., description="总学时")
    theory: int = Field(..., description="理论学时")
    practice: int = Field(..., description="实践学时")

class ScheduleSegment(BaseModel):
    """分段排课定义 — 同一班级在不同周次可有不同节次/星期"""
    weeks: str = Field(..., description="周次范围，支持: 范围'10-13' / 枚举'7,9' / 混合'7,9,11-13'")
    period: str = Field(..., description="节次，支持逗号分隔多时段如 '1-5节, 11-15节'")
    day: Optional[str] = Field(None, description="星期几（周一~周日），用于同一周多日上课场景。缺省时继承 schedule_time")

class ClassInfo(BaseModel):
    name: str = Field(..., description="班级名称")
    schedule_time: str = Field(..., description="上课时间（默认星期+节次，如'周四2-5节'或'星期日(分段排课)'）")
    schedule_segments: List[ScheduleSegment] = Field([], description="分段排课定义列表（Schema 2.2）")
    week_range: Optional[str] = Field(None, description="教学周次范围，如 '9-18'")
    excluded_weeks: List[int] = Field([], description="停课周次列表（节假日等）")
    official_weeks: Optional[int] = Field(None, description="教务注册周数（信息性字段）")
    classroom: Optional[str] = Field(None, description="教室")
    archive_id: Optional[int] = Field(None, description="班级归档序号（每学期由系部汇总表分配，用于云盘提交命名）")
    
class CourseIntroduction(BaseModel):
    content: str = Field(..., description="课程主要内容简介 (RichText)")
    design: str = Field(..., description="教学设计思路 (RichText)")

class CourseInfo(BaseModel):
    name: str = Field(..., description="课程名称")
    code: str = Field(..., description="课程代码")
    semester: str = Field(..., description="学期")
    nature: str = Field(..., description="课程性质 (必修/选修/专业课/专业选修/公共课/公共选修/成长课)")
    credits: float = Field(..., description="学分")
    classes: List[ClassInfo] = Field(..., description="授课班级列表")
    hours: CourseHours
    introduction: Optional[CourseIntroduction] = Field(None, description="课程简介与设计思路")
    resources_url: Optional[str] = Field(None, description="课程资源链接")
    department: str = Field("设计学院", description="开课单位")
    major: str = Field("数字媒体艺术", description="开课专业")
    prerequisites: str = Field("无", description="先修课程")

class TeacherInfo(BaseModel):
    name: str = Field(..., description="教师姓名")
    title: str = Field(..., description="职称")
    office: str = Field(..., description="办公室")
    phone: Optional[str] = Field(None, description="联系电话")
    archive_id: Optional[int] = Field(None, description="⚠️ 已废弃，迁移至 ClassInfo.archive_id。向后兼容保留")

class TeachingStep(BaseModel):
    # 兼容两套字段名: phase/content/method (schema原始) 和 stage/summary (实际YAML)
    phase: Optional[str] = Field(None, description="教学阶段 (导入/讲授/练习/总结)")
    stage: Optional[str] = Field(None, description="教学阶段 (复习/导入/讲授/演示/实践/小结)")
    content: Optional[str] = Field(None, description="教学内容")
    summary: Optional[str] = Field(None, description="教学内容摘要")
    method: Optional[str] = Field(None, description="教学方法")
    ideology: Optional[str] = Field(None, description="课程思政融入点")
    minutes: int = Field(..., description="预计时长 (分钟)")

    class Config:
        extra = 'allow'

class LessonUnit(BaseModel):
    topic: str = Field(..., description="单元主题")
    objectives: List[str] = Field([], description="本次课教学目标")
    steps: List[TeachingStep] = Field([], description="教学过程")
    review: Optional[str] = Field(None, description="课后作业/复习")

class CalendarWeek(BaseModel):
    week: int = Field(..., description="周次")
    date_range: Optional[str] = Field(None, description="日期范围")
    topic: str = Field(..., description="周主题")
    content: str = Field(..., description="详细内容 (主要知识点，需自带编号前缀)")
    chapter_title: Optional[str] = Field(None, description="章纯标题（不含前缀，如'交互体系概论基础'）。前缀（第X章/项目X）由 chapter_utils 根据学时类型自动合成")
    exp_id: Optional[int] = Field(None, description="关联实验 ID (对应 experiments[].id)")
    key_points: Optional[str] = Field(None, description="重点/难点")
    hours_theory: int = Field(0, description="本单元理论学时")
    hours_practice: int = Field(0, description="本单元实践学时")
    
    task: Optional[str] = Field(None, description="课后作业/任务")
    homework: Optional[str] = Field(None, description="详细作业要求")
    has_homework: bool = Field(False, description="是否有作业")
    method: Optional[str] = Field(None, description="教学方法")
    lessons: List[LessonUnit] = Field([], description="教学单元列表 (通常每周包含1-2个单元)")
    # 以下字段用于"三、课程内容和教学要求"章节渲染 (Comment 16)
    teaching_requirements: Optional[Any] = Field(None, description="教学要求")
    focus: Optional[str] = Field(None, description="重点")
    difficulty: Optional[str] = Field(None, description="难点")
    ideology: Optional[str] = Field(None, description="课程思政融入点")
    teaching_method: Optional[str] = Field(None, description="采用的教学方法 (如案例演示、小组讨论等)")
    readings: Optional[List[str]] = Field(None, description="本周指定阅读教材与章节（如：'《交互设计》第1章'）。生成器将优先使用此字段，缺失时会尝试自动从 objectives 和 content 中提取")

    class Config:
        extra = 'allow'

class Experiment(BaseModel):
    id: int = Field(..., description="实验序号")
    name: str = Field(..., description="实验名称")
    type: str = Field(..., description="实验类型")
    hours: int = Field(..., description="实验学时")
    group_size: int = Field(1, alias="group", description="每组人数") # 'group' in yaml
    requirement: Optional[str] = Field("必做", description="必做/选做")

class TextbookChapter(BaseModel):
    """教材目录章节条目 — Phase 2a 新增，用于结构化引用教材章节标题"""
    chapter: Union[int, str] = Field(..., description="章节号（数字或字符串，适配无编号教材如 Refactoring UI）")
    title: str = Field(..., description="章节标题（中文）")
    title_en: Optional[str] = Field(None, description="英文原标题（外文教材可选，便于交叉校验）")

class Textbook(BaseModel):
    title: str = Field(..., description="教材名称")
    author: str = Field(..., description="作者")
    publisher: str = Field(..., description="出版社")
    isbn: Optional[str] = Field(None, description="ISBN")
    year: str = Field(..., description="出版年份")
    type: str = Field("textbook", description="类型: textbook(教材)/reference(参考书)")
    toc: Optional[List[TextbookChapter]] = Field(None, description="教材目录结构（Phase 2a 新增）。用于三份文档的教材章节引用标准化")

class SemesterConfig(BaseModel):
    start_date: str = Field(..., description="学期开始日期 (YYYY-MM-DD)")

class Question(BaseModel):
    content: str = Field(..., description="题目内容")
    type: str = Field(..., description="题型 (选择/填空/简答/计算/设计)")
    options: Optional[List[str]] = Field(None, description="选项 (仅选择题)")
    answer: Optional[str] = Field(None, description="参考答案")
    score: float = Field(..., description="分值")

class ExamSection(BaseModel):
    section_name: str = Field(..., description="大题名称 (一、选择题)")
    questions: List[Question] = Field(..., description="题目列表")
    total_score: float = Field(..., description="该大题总分")

class ExamPaper(BaseModel):
    name: str = Field(..., description="试卷名称 (A卷/B卷)")
    duration: int = Field(120, description="考试时长 (分钟)")
    total_score: float = Field(100, description="卷面总分")
    sections: List[ExamSection] = Field(..., description="试卷结构")

class ExamConfig(BaseModel):
    final_exam: List[ExamPaper] = Field(..., description="期末试卷列表 (A卷, B卷)")

class AssessmentItem(BaseModel):
    name: str = Field(..., description="项目名称")
    ratio: float = Field(..., description="占平时成绩的比例 (%)")
    desc: Optional[str] = Field(None, description="评分标准")

    @validator('name')
    def check_name_format(cls, v):
        """ADR 005: name 格式应为 '章节测试N' 或 '命题测试N'"""
        import re
        if not re.match(r'^(章节测试|命题测试)\d+$', v) and v != '考勤':
            print(f"  ⚠️  [WARNING] AssessmentItem.name='{v}' 不符合命名规范 (应为 '章节测试N' 或 '命题测试N')")
        return v

    @validator('desc')
    def check_desc_has_experiment_ref(cls, v):
        """ADR 005: desc 应包含 '对应实验' 关键词以关联外键"""
        if v and '对应实验' not in v and '考勤' not in v:
            print(f"  ⚠️  [WARNING] AssessmentItem.desc 缺少 '对应实验N' 外键关联")
        return v

class AssessmentMethods(BaseModel):
    normal_score_ratio: float = Field(..., description="平时成绩占比 (%)")
    final_score_ratio: float = Field(..., description="期末成绩占比 (%)")
    attendance_ratio: float = Field(10.0, description="考勤占比 (默认10%)")
    normal_items: List[AssessmentItem] = Field(..., description="平时成绩构成项 (不含考勤)")

    @root_validator(skip_on_failure=True)
    def check_ratios_sum_to_100(cls, values):
        normal = values.get('normal_score_ratio')
        final = values.get('final_score_ratio')
        if normal is not None and final is not None:
            if abs(normal + final - 100) > 0.01:
                raise ValueError(f"总成绩比例之和 ({normal} + {final}) 必须等于 100")
        
        items = values.get('normal_items')
        attendance = values.get('attendance_ratio', 0)
        
        if items and normal is not None:
            total_items = sum(item.ratio for item in items) + attendance
            if abs(total_items - normal) > 0.01:
                 raise ValueError(f"平时成绩各分项(含考勤{attendance}%)比例之和 ({total_items}) 必须等于平时成绩占比 ({normal})")
        
        return values

class ObjectiveMapping(BaseModel):
    """单条毕业要求映射（一个课程目标可映射多条）"""
    requirement: str = Field(..., description="对应毕业要求")
    point: str = Field(..., description="对应观测点")
    support_level: str = Field('', description="支撑强度 (H/M/L)")

class ObjectiveItem(BaseModel):
    index: int = Field(..., description="序号")
    desc: str = Field(..., description="目标描述")
    mappings: List[ObjectiveMapping] = Field([], description="毕业要求映射列表")

    def get_mappings(self) -> list:
        """获取映射列表。"""
        return [m.dict() for m in self.mappings]

class CourseObjectives(BaseModel):
    knowledge: List[ObjectiveItem] = Field([], description="知识目标")
    ability: List[ObjectiveItem] = Field([], description="能力目标")
    quality: List[ObjectiveItem] = Field([], description="素质目标")

class CourseSchema(BaseModel):
    course: CourseInfo
    teacher: TeacherInfo
    objectives: Optional[CourseObjectives] = Field(None, description="课程目标 (3维矩阵)")
    student_analysis: Optional[str] = Field(None, description="学情分析")
    
    calendar: List[CalendarWeek]
    experiments: List[Experiment] = Field([], description="实验项目列表")
    textbooks: List[Textbook] = Field([], description="教材与参考书")
    semester_config: Optional[SemesterConfig] = Field(None, description="学期时间配置")
    assessment_methods: Optional[AssessmentMethods] = Field(None, description="考核方式")
    exams: Optional[ExamConfig] = Field(None, description="考试配置")

    @root_validator(skip_on_failure=True, pre=True)
    def ensure_exams_exists(cls, values):
        """ADR 004: exams 为模板渲染必需字段，缺失时构造最小空结构"""
        if 'exams' not in values or values['exams'] is None:
            print("  ⚠️  [WARNING] 缺少 'exams' 节点，已自动构造空结构。请补充完整的考试/考查配置。")
            values['exams'] = {
                'final_exam': [{
                    'name': '期末考查',
                    'duration': 0,
                    'total_score': 100,
                    'sections': [{
                        'section_name': '考查',
                        'total_score': 100,
                        'questions': [{'content': '待填写', 'type': '设计', 'score': 100}]
                    }]
                }]
            }
        return values

    @root_validator(skip_on_failure=True)
    def check_hours_consistency(cls, values):
        course = values.get('course')
        calendar = values.get('calendar')
        
        if course:
            # 1. Total check
            if course.hours.total != course.hours.theory + course.hours.practice:
                raise ValueError(f"总学时({course.hours.total}) 不等于 理论({course.hours.theory}) + 实践({course.hours.practice}) 之和")
            
            # 2. Calendar Sum check
            if calendar:
                cal_theory = sum(w.hours_theory for w in calendar)
                cal_practice = sum(w.hours_practice for w in calendar)
                
                # Allow a small buffer or check exact? Ideally exact.
                # But some weeks might not be fully populated yet. 
                # Let's emit a warning-like error if strict. For now enforce exactness for consistency.
                if cal_theory != course.hours.theory:
                     raise ValueError(f"Calendar理论学时总和({cal_theory}) 不等于 课程设定值({course.hours.theory})")
                
                if cal_practice != course.hours.practice:
                     raise ValueError(f"Calendar实践学时总和({cal_practice}) 不等于 课程设定值({course.hours.practice})")

        return values

    @root_validator(skip_on_failure=True)
    def check_experiment_hours(cls, values):
        experiments = values.get('experiments')
        course = values.get('course')
        if experiments and course:
            exp_total = sum(e.hours for e in experiments)
            if exp_total > course.hours.practice:
                raise ValueError(f"实验总学时({exp_total}) 超过了课程实践学时({course.hours.practice})")
        return values
