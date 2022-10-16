import best_lib

balance = best_lib.Balance()

my_resp = best_lib.make_report('https://habr.com/ru/company/vk/blog/692062/')
my_resp2 = best_lib.make_report('https://jsonplaceholder.typicode.com/posts/1/')

print(f'Текст my_resp:\n {my_resp.text}')
print(f'Текст my_resp2:\n {my_resp2.text}')
print(f'Статус кода my_resp:\n {my_resp.status_code}')
print(f'Статус кода my_resp2:\n {my_resp2.status_code}')
