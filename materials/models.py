from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса', **NULLABLE)
    preview = models.ImageField(upload_to='images/preview_course/', **NULLABLE, verbose_name='Превью курса')

    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока', **NULLABLE)
    preview = models.ImageField(upload_to='images/preview_lesson/', **NULLABLE, verbose_name='Превью урока')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='Курс')



    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.name}, {self.course}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
