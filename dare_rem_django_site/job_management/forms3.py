from django import forms
from .models import FileTransfer
import os
import itertools
def get_file_list(path):
    files = []
    i=0
    ilia=[]
    dictionary={}
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path,name)):
            i=i+1
            files.append(name)
            ilia.append(i)
    dictionary=dict(itertools.izip(ilia,files))
    file_list=dictionary.items()        
    return file_list

class FileTransferForm(forms.Form):
    #path= "/home/cctsg/software/DARE-NGS/test"
    #file_list=get_file_list(path)
    def __init__(self, *args, **kwargs):
       path= "/home/cctsg/software/DARE-NGS/darengs/lib/DARE/darefiles/1"
       file_list=get_file_list(path)
       super(FileTransferForm, self).__init__(*args, **kwargs)
       #self.fields['Files']=forms.ChoiceField(choices=file_list)
       self.fields['Files']=forms.MultipleChoiceField(choices=file_list,widget=forms.CheckboxSelectMultiple())
 
#class FinalFileTransferForm(forms.ModelForm):
    #form=FileTransferForm
    #class Meta:
        #model=FileTransfer  
