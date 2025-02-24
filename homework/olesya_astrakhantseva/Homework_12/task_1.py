class Flower:
    def __init__(self, name, height, lifetime, price, need_water, color):
        self.name = name
        self.height = height
        self.lifetime = lifetime
        self.price = price
        self.need_water = need_water
        self.color = color


class Rose(Flower):
    def __init__(self, name, height, lifetime, price, need_water,
                 color, petal_count, rose_type):
        super().__init__(name, height, lifetime, price, need_water, color)
        self.petal_count = petal_count
        self.rose_type = rose_type


class Tulip(Flower):
    def __init__(self, name, height, lifetime, price, need_water,
                 color, flower_shape, cup_color):
        super().__init__(name, height, lifetime, price, need_water, color)
        self.flower_shape = flower_shape
        self.cup_color = cup_color


class Sunflower(Flower):
    def __init__(self, name, height, lifetime, price, need_water,
                 color, seed_size, sun_tracking_angle):
        super().__init__(name, height, lifetime, price, need_water, color)
        self.seed_size = seed_size
        self.sun_tracking_angle = sun_tracking_angle


class Buket:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calc_price(self):
        return sum(flower.price for flower in self.flowers)

    def average_lifetime(self):
        total_lifetime = sum(flower.lifetime for flower in self.flowers)
        return total_lifetime / len(self.flowers)

    def sort_by_lifetime(self):
        self.flowers.sort(key=lambda flower: flower.lifetime)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_height(self):
        self.flowers.sort(key=lambda flower: flower.height)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def find_flowers_by_lifetime(self, min_lifetime, max_lifetime):
        return [flower for flower in self.flowers
                if min_lifetime <= flower.lifetime <= max_lifetime]


rose = Rose(
    name="Роза", height=50, lifetime=7, price=100, need_water=True,
    color="красный", petal_count=30, rose_type="чайная"
)
tulip = Tulip(
    name="Тюльпан", height=30, lifetime=5, price=50, need_water=False,
    color="желтый", flower_shape="классический", cup_color="зеленый"
)
sunflower = Sunflower(
    name="Подсолнух", height=150, lifetime=10, price=80, need_water=True,
    color="желтый", seed_size="большой", sun_tracking_angle=180
)

bouquet = Buket()
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(sunflower)

print(f"Стоимость букета: {bouquet.calc_price()} р")
print(f"Среднее время увядания букета: {round(bouquet.average_lifetime())} минут")

bouquet.sort_by_lifetime()
print("Цветы после сортировки по времени жизни:")
for flower in bouquet.flowers:
    print(f"- {flower.name}, время жизни: {flower.lifetime} минут")

found_flowers = bouquet.find_flowers_by_lifetime(min_lifetime=6, max_lifetime=12)
print("Найденные цветы с временем жизни от 6 до 12 дней:")
for flower in found_flowers:
    print(f"- {flower.name}")
