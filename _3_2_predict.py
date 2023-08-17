import torch
from transformers import RobertaForSequenceClassification, AutoTokenizer
model = RobertaForSequenceClassification.from_pretrained("Custom_model")
tokenizer = AutoTokenizer.from_pretrained("wonrax/phobert-base-vietnamese-sentiment", use_fast=False)
from _2_1_pre_processing import read_input, word_segment

# Just like PhoBERT: INPUT TEXT MUST BE ALREADY WORD-SEGMENTED!

#sentence = 'Đây là mô hình rất hay , phù hợp với điều kiện và nhu cầu của nhiều người .'  
#sentence = 'đang dạy Thầy wzjwz208 đi qua nước ngoài giữa chừng , thầy Wzjwz209 dạy thay .'
# sentence = 'Thầy dạy hay'
def run(sentence):
    
    sentence = read_input(sentence)
    #sentence = word_segment(sentence)

    input_ids = torch.tensor([tokenizer.encode(sentence)])

    with torch.no_grad():
        out = model(input_ids)
        #print(out)
        # print(out.logits.softmax(dim=-1).tolist())
        return out.logits.softmax(dim=-1).tolist()[0]
        # Output:
        # [[0.002, 0.988, 0.01]]
        #     ^      ^      ^
        #    NEG    NEU    POS