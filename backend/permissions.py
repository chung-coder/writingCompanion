from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    """
    Student Permission
    - Ensures the user is logged in and has a student profile
    - Used to restrict access to student-only features
    """
    def has_permission(self, request, view):
        return bool(request.user and hasattr(request.user, 'student'))

class IsTeacher(BasePermission):
    """
    Teacher Permission
    - Ensures the user is logged in and has a teacher profile
    - Used to restrict access to teacher-only features
    """
    def has_permission(self, request, view):
        return bool(request.user and hasattr(request.user, 'teacher'))

class IsTeacherOrOwner(BasePermission):
    """
    Teacher or Resource Owner Permission
    - Teachers can access their students' resources
    - Students can access their own resources
    
    Applicable to:
    - Diary
    - Student Profile
    - GPT Interaction Records (GPTInteraction, GPTAssistance)
    """
    def has_object_permission(self, request, view, obj):
        user = request.user
        
        # Check if user is a teacher
        if hasattr(user, 'teacher'):
            # Check if accessing their student's resources
            if hasattr(obj, 'student'):
                return obj.student.teacher_id == user.teacher.id
            if hasattr(obj, 'teacher'):
                return obj.teacher_id == user.teacher.id
            return False
            
        # Check if user is a student
        if hasattr(user, 'student'):
            # Check if accessing their own resources
            if hasattr(obj, 'student'):
                return obj.student.user_id == user.id
            return obj.user_id == user.id
            
        return False