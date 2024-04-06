non_token = ['$2','$1','$3',';']
token_list = ["E","$2","E"]
new_token_list = [ item for item in token_list if not any( item == garbage for garbage in non_token )]
print(new_token_list)