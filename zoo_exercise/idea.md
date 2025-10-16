Třída Zoo():
- Atributs:
  - opening_hours
  - pricing
- Methods:
  - info() - vypíše info o ceníku a otevírací době
  - add_animal() - přídá nové zvíře do ZOO
  - animals() - vypíše všechna zvířata ze ZOO

Animal()
- hlavní třída od které se bude odvíjet veškerá zvířata
- Atributs:
  - name
  - type
  - age
  - size
  - weight
- Methods:
  - sleep()
  - eat()
  - make_sound()

subtřídy jako Tiger(), Lion(), Elephant(), Snake()
- budou dědit z Animal()
- upravené metody (polymorphismus)

