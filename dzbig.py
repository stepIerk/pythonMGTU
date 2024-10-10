
def analyzer(h, m):
    hours_text = ''
    minutes_text = ''
    time_text = ''
    special_text = ''
    out_m = str(m)
    out_h = h
    if h > 23 or m > 59:
        return 'invalid data'
    else:
        if h < 5:
            time_text = 'ночи'
        elif h < 12:
            time_text = 'утра'
        elif h < 18:
            time_text = 'дня'
        else:
            time_text = 'вечера'
            
        if h > 12:
            out_h = h - 12
            
        if out_h == 1:
            hours_text = 'час'
        elif out_h < 5:
            hours_text = 'часа'
        else:
            hours_text = 'часов'

        if m == 0:
            out_m = ''
            if out_h == 0:
                hours_text = 'полночь'
                time_text = '' 
                out_h = '' 
            elif out_h == 12:
                hours_text = 'полдень'
                time_text = ''
                out_h = ''
            else:
                special_text = 'ровно'
        else:
            if m%10 == 1:
                minutes_text = 'минута'
            elif m%10 < 5:
                minutes_text = 'минуты'
            else:
                minutes_text = 'минут'
        return(out_h, hours_text, out_m, minutes_text, time_text, special_text)
        
try:
    input_h, input_m = input('Enter time >>> ').split()
    hours = int(input_h)
    minutes = int(input_m)
    ans = ' '.join(filter(None, [str(s) for s in analyzer(hours, minutes)]))
    print(input_h, input_m, '-', ans)
except:
    print('invalid data')
