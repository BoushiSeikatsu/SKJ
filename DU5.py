import xml.etree.ElementTree as ET

def create_student(xml_root, student_id):
    '''
    Vytvořte studenta dle loginu.
    Ujistěte se, že student neexistuje, jinak: raise Exception('student already exists')
    '''
    for child in xml_root:
        if(child.attrib["student_id"] == student_id):
            raise Exception("student already exists")
    student = ET.Element('student')
    student.set('student_id', student_id)
    xml_root.append(student)
    pass


def remove_student(xml_root, student_id):
    '''
    Odstraňte studenta dle loginu
    '''
    for student in xml_root:
        if(student.attrib["student_id"] == student_id):
            xml_root.remove(student)
    pass


def set_task_points(xml_root, student_id, task_id, points):
    '''
    Přepište body danému studentovi u jednoho tasku
    '''
    findStudentString = "student[@student_id='{toFind}']".format(toFind = student_id)
    targetStudent = xml_root.find(findStudentString)
    findTargetString = "task[@task_id='{toFind}']".format(toFind = task_id)
    targetTask = targetStudent.find(findTargetString)
    targetTask.text = points
    pass


def create_task(xml_root, student_id, task_id, points):
    '''
    Pro daného studenta vytvořte task s body.
    Ujistěte se, že task (s task_id) u studenta neexistuje, jinak: raise Exception('task already exists')
    '''
    findStudentString = "student[@student_id='{toFind}']".format(toFind = student_id)
    targetStudent = xml_root.find(findStudentString)
    for task in targetStudent:
        if(task.attrib["task_id"] == task_id):
            raise Exception("task already exists")
    taskToBeAdded = ET.SubElement(targetStudent, "task")
    taskToBeAdded.set("task_id", task_id)
    taskToBeAdded.text = points
    pass


def remove_task(xml_root, task_id):
    '''
    Napříč všemi studenty smažte task s daným task_id
    '''
    #findTargetString = "student/task[@task_id='{toFind}']".format(toFind = task_id)
    #targetTasks = xml_root.findall(findTargetString)
    for student in xml_root:
        findTargetString = "task[@task_id='{toFind}']".format(toFind = task_id)
        targetTask = student.find(findTargetString)
        if(targetTask is not None):
            student.remove(targetTask)
    pass
"""
tree = ET.parse('skj_class.xml')
root = tree.getroot()
create_student(root, 'DUB0074')
#print (ET.tostring(root))
remove_student(root, 'DUB0074')
#print (ET.tostring(root))
set_task_points(root, 'ABC0123', "1", 5)
#	print (ET.tostring(root))
create_task(root, "ABC0123", "9", "5")
#print (ET.tostring(root))
remove_task(root, "5")
#print (ET.tostring(root))"""