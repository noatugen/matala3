import json 
 
def read_file():
    file = open("WhatsApp2.txt" ,encoding='utf8')
    return file
           
        
def what_App(): 
    file = read_file()  
    number_id=1
    date=0
    index=0
    dic_id=dict()
    dic=dict()
    data_dic=dict()
    list_dic=list()
    for line in file:
        line=line.strip()
        if not ':' in line:
            dic['datetime']= date
            dic['id']=index
            dic['text'] =line  
            list_dic.append(dic.copy())
            continue
        first=line.find('-')+1
        stop=line.find(':',first)        
        if stop>0:    
            name=line[first:stop]   
            if name not in dic_id:
                dic_id[name]=number_id
                number_id=number_id+1
                # space=line[0:17]
                space = line.split()
                date_time = space[0] + " " + space[1]
                date_time=date_time.replace(',','')
                dic['datetime']= date_time
                dic['id']=number_id-1
                text = line.split(':')
                dic['text'] = text[2]  
                date=date_time
                index=number_id-1
                list_dic.append(dic.copy()) 
            else:
                dic['id']=dic_id[name]
         
                # space=line[0:17]
                space = line.split()
                date_time = space[0] + " " + space[1]
                date_time=date_time.replace(',','')
                dic['datetime']= date_time
                text = line.split(':')
                dic['text'] = text[2]  
                date=date_time
                list_dic.append(dic.copy()) 
                

    load_file = read_file()
    for line_r in load_file:
        line_r=line_r.strip()
        if 'נוצרה על ידי' in line_r:
            start=line_r.find('"')
            end=line_r.find('"',start)
            if end>0:
                find_creator=line_r.split('ידי')
                creation_date1=line_r.split()
                creation_date1=creation_date1[0] + " " + creation_date1[1]
                creation_date1=creation_date1.replace(',','')
                
                c_name=line_r.split('"')
                c_name=c_name[1].split('"')
                data_dic['chat_name']=c_name[0]
                data_dic['creation_date']=creation_date1
                data_dic['num_of_participants']=number_id-1
                data_dic['creator']=find_creator[1]
               

            chat_name1=c_name[0]
#חלק ה          
    final=dict()
    final['messages']=list_dic
    final['metadata']=data_dic

    json_file=chat_name1+".txt"       
    with open(json_file, 'w' , encoding='utf8') as json_file:
        json.dump( final,  json_file , ensure_ascii=False)
              

what_App()
