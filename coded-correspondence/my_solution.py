import decode
#fisrt message
message1 = 'jxu evviuj veh iusedt cuiiqwu yi vekhjuud.'
offset1 = 10
#print(decode.decode(message1,offset1))
offset2 = 14
messsage2 = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqoqdq!'
#print(decode.decode(messsage2,offset2))
reply = "Ok, thank you for your perfect advises. Now I will focus on making algorithm with multiple chispers!"
import encode
coded_reply = encode.code(reply,10)
de_coded_reply = decode.decode(coded_reply,10)
#print(de_coded_reply)

#unknown_code is 7
unknown_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
#print(decode.decode(unknown_message, 7))

import vigenere_chiper
message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
keyword = "friends"
print(vigenere_chiper.decode_vinegre(message,keyword))

import viniger_coder
#message = "Jestem Malgorzata i gotuje obiad!"
#keyword = "Lesiu"
#coded_message = viniger_coder.code_vinegre(message,keyword)
#print(coded_message)

#print(vigenere_chiper.decode_vinegre(coded_message,keyword))

# CAŁY PROJEKT ZROBIONY, AVE MARIA





       








