import discord
from discord.ext import commands
from math import ceil
import random
import json
import DiscordUtils

points = ['Points', 250, 228, 210, 195, 180, 170, 160, 151, 144, 137, 132, 127, 123.6, 120.2, 117.4, 115, 112.9, 111,
          109.5, 108.2, 107, 105.7, 104.5, 103.23, 101.94, 100.6, 99.3, 98, 96.6, 95.2, 94, 92.5, 91.5, 89.6, 88.2,
          86.6, 85.1, 83.6, 82, 80.5, 78.9, 77.3, 75.7, 74, 72.3, 70.7, 69, 67.2, 65.5, 63.7, 61.9, 60.1, 58.5, 56.9,
          55.3, 53.9, 52.3, 50.8, 49.4, 48, 46.7, 45.4, 44.2, 43, 41.8, 40.7, 39.5, 38.5, 37.4, 36.4, 35.4, 34.4, 33.5,
          32.6, 31.7, 30.9, 30, 29.2, 28.4, 27.7, 27, 26.2, 25.6, 25, 24.2, 23.5, 23, 22.3, 21.7, 21.2, 20.6, 20, 19.5,
          19, 18.5, 18, 17.6, 17.1, 16.7, 16.3]


with open('demonlist.json', 'r') as f:
  demonlist = json.load(f)
dl = demonlist["dl"]

print(dl)


def refresh_demonlist():
    dl_pages = []
    dl_embed_pages = []

    print(len(dl))
    print(dl[5][2][0][1])
    if len(dl) >= 100:
        for i in range(10):
            dl_pages.append(f"**Place | {dl[0][0]} | {dl[0][1]} | {dl[0][2]}**\n")
            for j in range(10):
                try:
                    index = int(f"{str(i)}{str(j)}") + 1
                    victors = ''
                    for n in range(len(dl[index][2])):
                        if dl[index][2][n][1] == '':
                            victors += f"**{dl[index][2][n][0]}**, "
                        else:
                            victors += f"**[{dl[index][2][n][0]}]({dl[index][2][n][1]})**, "
                    victors = victors[:-2]
                    dl_pages[i] += f"***#{index}*** **|** **{dl[index][0]}** by **{dl[index][1]}** **|** {points[index]}p\n" \
                                   f"Victors: {victors}\n\n"
                except IndexError:
                    break
    else:
        print(len(dl) // 10)
        for i in range(ceil(len(dl) / 10)):
            dl_pages.append(f"**Place | {dl[0][0]} | {dl[0][1]} | {dl[0][2]}**\n")
            for j in range(10):
                try:
                    index = int(f"{str(i)}{str(j)}") + 1
                    victors = ''
                    for n in range(len(dl[index][2])):
                        if dl[index][2][n][1] == '':
                            victors += f"{dl[index][2][n][0]}, "
                        else:
                            victors += f"[{dl[index][2][n][0]}]({dl[index][2][n][1]}), "
                    victors = victors[:-2]
                    dl_pages[i] += f"**#{index} {points[index]}p | {dl[index][0]} by {dl[index][1]}\n" \
                                   f"Victors:** {victors}\n\n"
                except IndexError:
                    break

    for i in range(len(dl_pages)):
        dl_embed_pages.append(discord.Embed(
            title='Официальный демонлист GMD | Общение',
            description=dl_pages[i],
            colour=discord.Colour.purple()
        ))

    return dl_embed_pages


def refresh_stats():
    players_pages = []
    players_embed_pages = []
    players_names = []
    players_points = []
    players_count = []
    players_completions = []
    players_main = []
    players_extended = []
    players_legacy = []
    players = {}


    for i in dl:
        if i[2] == 'Victors':
            continue
        for j in i[2]:
            if j[0] not in players:
                players[j[0]] = [0, 0, [], 0, 0, 0]

    print(players)

    for player in players:
        if len(dl) > 100:
            for i in range(len(dl)):
                for j in range(len(dl[i][2])):
                    print(dl[i][2][j][0])
                    if player.lower() in dl[i][2][j][0].lower():
                        if i < 101:
                          players[player][0] += points[i]
                        players[player][1] += 1
                        if i <= 50:
                            players[player][2].append(f"**{dl[i][0]}**")
                            players[player][3] += 1
                        elif 100 >= i > 50:
                            players[player][2].append(dl[i][0])
                            players[player][4] += 1
                        else:
                            players[player][2].append(f"*{dl[i][0]}*")
                            players[player][5] += 1
        else:
            for i in range(len(dl)):
                if dl[2] == 'Victors':
                    continue
                for j in range(len(dl[i][2])):
                    if player.lower() in dl[i][2][j][0].lower():
                        players[player][0] += points[i]
                        players[player][1] += 1
                        if i <= 50:
                            players[player][2].append(f"**{dl[i][0]}**")
                            players[player][3] += 1
                        elif 100 >= i > 50:
                            players[player][2].append(dl[i][0])
                            players[player][4] += 1
                        else:
                            players[player][2].append(f"*{dl[i][0]}*")
                            players[player][5] += 1

    sorted_players = {k: v for k, v in sorted(players.items(), key=lambda item: item[1][0], reverse=True)}
    print(sorted_players)

    for key, value in sorted_players.items():
        players_names.append(key)
        players_points.append(round(value[0], 2))
        players_count.append(value[1])
        players_completions.append(value[2])
        players_main.append(value[3])
        players_extended.append(value[4])
        players_legacy.append(value[5])

    for i in range(ceil(len(players) / 10)):
        players_pages.append("")
        for j in range(10):
            index = int(f"{str(i)}{str(j)}")
            try:
                players_pages[i] += f"**#{index + 1} {players_names[index]}** - {players_points[index]}p |" \
                                    f" {players_count[index]} :DEMON:\n\n"
            except IndexError:
                break

    print(players_pages)

    print(players_pages)
    print(players_embed_pages)

    return players_pages, players, players_names, players_completions, players_count, players_points,\
           players_main, players_extended, players_legacy


def refresh_legacy():
    if len(dl) > 100:
        legacy_pages = [""]
        legacy_embed_pages = []

        current = 0
        for i in range(101, len(dl)):
            try:
                if i % 10 == 0:
                    legacy_pages.append("")
                    current += 1
                index = i
                print(index)
                victors = ''
                for n in range(len(dl[index][2])):
                    if dl[index][2][n][1] == '':
                        victors += f"{dl[index][2][n][0]}, "
                    else:
                        victors += f"[{dl[index][2][n][0]}]({dl[index][2][n][1]}), "
                victors = victors[:-2]
                legacy_pages[current] += f"**#{index} | {dl[index][0]} by {dl[index][1]}\n" \
                                   f"Victors:** {victors}\n\n"
            except IndexError:
                break

        for i in range(len(legacy_pages)):
            legacy_embed_pages.append(discord.Embed(
                title='Официальный демонлист GMD | Общение',
                description=legacy_pages[i],
                colour=discord.Colour.purple()
            ))

        return legacy_embed_pages

    else:
        return [discord.Embed(
            title="Ошибка!",
            description="Легаси листа не существует!",
            colour=discord.Colour.purple())]


dl_embed = refresh_demonlist()
players_pages, players, players_names, players_completions, players_count, players_points,\
           players_main, players_extended, players_legacy = refresh_stats()
legacy_embed = refresh_legacy()

print(dl[5])


# Commands
class Demonlist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Demonlist cog loaded')

    @commands.command(aliases=[
        "дл", "демонлист", "ДЛ", "ДЕМОНЛИСТ", "Дл", "Демонлист", 'DL', "Dl", "Demonlist", "demonlist", "DEMONLIST"
    ])
    async def dl(self, ctx, index=1):
        buttons = [u"\25C0", u"\25B6"]
        rnd = random.randint(1, 10)
        print(rnd)
        if rnd == 7:
            await ctx.send('ХУЙ ТЕБЕ А НЕ ДЕМОНЛИСТ')
        else:
            dl_embed = refresh_demonlist()
            index -= 1
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
            paginator.add_reaction('⏮️', "first")
            paginator.add_reaction('⏪', "back")
            paginator.add_reaction('⏩', "next")
            paginator.add_reaction('⏭️', "last")
            await paginator.run(dl_embed)

    @commands.command(aliases=["легаси", "ЛЕГАСИ", "Легаси", "LEGACY", "Legacy"])
    async def legacy(self, ctx, index=1):
        legacy_embed = refresh_legacy()
        index -= 1
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction('⏮️', "first")
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('⏭️', "last")
        await paginator.run(legacy_embed)

    @commands.command(aliases=['STATS', 'Stats', "стата", "СТАТА", "Стата"])
    async def stats(self, ctx, index=1):
        players_pages, players, players_names, players_completions, players_count, players_points,\
           players_main, players_extended, players_legacy = refresh_stats()
      
        emojis = {e.name: str(e) for e in ctx.bot.emojis}

        players_embed = []
        for i in range(len(players_pages)):
          players_embed.append(discord.Embed(
            title='Официальный топ игроков GMD | Общение',
            description=players_pages[i].replace(":DEMON:", emojis["DEMON"]),
            colour=discord.Colour.purple()
          ))
      
        index -= 1
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction('⏮️', "first")
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('⏭️', "last")
        await paginator.run(players_embed)

    @commands.command(aliases=['профиль', "ПРОФИЛЬ", "Профиль", 'Profile', "PROFILE"])
    async def profile(self, ctx, player: str):
        players_embed, players, players_names, players_completions, players_count, players_points,\
           players_main, players_extended, players_legacy = refresh_stats()

        lower_names = [i.lower() for i in players_names]
        print(lower_names)
        if player.lower() in lower_names:
            index = lower_names.index(player.lower())

            completions = ''
            for i in players_completions[index]:
                completions += f'{i}, '
            completions = completions[:-2]

            await ctx.send(embed=discord.Embed(
                title=f'Профиль игрока {players_names[index]}',
                description=f"\nМесто: **#{index + 1}**\n"
                            f"Количество поинтов: **{players_points[index]}p**\n"
                            f"Всего пройдено уровней: **{players_count[index]}**\n Main: **{players_main[index]}**\n \
                            Extended: **{players_extended[index]}**\n Legacy: **{players_legacy[index]}**\n\n"
                            f"Хардест: {players_completions[index][0]}\n"
                            f"Пройденые уровни: {completions}",
                colour=discord.Colour.purple()
            ))
        else:
            await ctx.send("Игрок не найден!")

    @commands.command(aliases=['рулетка', "РУЛЕТКА", "Рулетка"])
    async def roulette(self, ctx, percent="None"):
        percent = str(percent)
        player = str(ctx.author.id)

        with open('roulette_percent.json', 'r') as f:
            roulette_players = json.load(f)

        with open('played_roulette_levels.json', 'r') as f:
            roulette_levels = json.load(f)

        print(roulette_levels)
        print(percent)

        if "%" in percent:
            percent = percent.replace("%", "")
        if "сброс" in percent.lower():
            await ctx.send(f"Ваша игра в рулетку завершается на {len(roulette_levels[player])} очках. Ваша рулетка сброшена. Вызовите еще раз команду чтоб начать игру!")
            roulette_players[player] = 0
            roulette_levels[player] = []

            with open('roulette_percent.json', 'w') as f:
                json.dump(roulette_players, f, indent=4)

            with open('played_roulette_levels.json', 'w') as f:
                json.dump(roulette_levels, f, indent=4)

            return 0

        if percent == "None":
            percent = 0

        try:
            percent = int(percent)
        except ValueError:
            print('Converting to "int" failed for parameter "percent".')

        while True:
            level = random.choice(dl)
            name = level[0]
            author = level[1]
            if player not in roulette_players:
              break
            elif name != dl[0][0] and name not in roulette_levels[player]:
                break

        print(player)
        print(roulette_players.keys())
        if player in roulette_players:
            print(5)
            if percent > 100:
              await ctx.send("ты кому пиздишь падла?")
              return 0
            elif percent == 100:
              await ctx.send(f"Вы прошли рулетку демонов! Поздравляю! Всего на вашем пути было {len(roulette_levels[player])} уровней")
              await ctx.send(f"Ваша игра в рулетку завершается на {len(roulette_levels[player])} очках. Ваша рулетка сброшена. Вызовите еще раз команду чтоб начать игру!")
              roulette_players[player] = 0
              roulette_levels[player] = []
            elif roulette_players[player] > percent:
                print(55)
                await ctx.send(f"Вы должны поставить больше {roulette_players[player]}%. Указанный вам процент меньше вашего"
                         f" предыдушего рекорда.")
                return 0
            else:
                print(44)
                roulette_players[player] = percent + 1
                roulette_levels[player].append(name)
        else:
            print(4)
            roulette_players[player] = 0
            roulette_levels[player] = []

        print(name)

        with open('roulette_percent.json', 'w') as f:
            json.dump(roulette_players, f, indent=4)

        with open('played_roulette_levels.json', 'w') as f:
            json.dump(roulette_levels, f, indent=4)

        await ctx.send(embed=discord.Embed(
            title='Рулетка ГМДО Демонлиста',
            description=f"Уровень #{len(roulette_levels[player])}: **{name}** by **{author}**. Вам нужно поставить **{percent + 1}%** или больше",
            colour=discord.Colour.purple()
        ))

    @commands.command(aliases=["Add", "ADD", "добавить", "ДОБАВИТЬ", "Добавить"])
    @commands.has_role("РЕДАКТОР ДЕМОНЛИСТА")
    async def add(self, ctx, index: int, victor: str, author: str, *, name: str):
        dl.insert(int(index), [name, author, [[victor, '']]])
        await ctx.send(f"{name} успешно поставлен на {index} место!")

        demonlist["dl"] = dl
        with open('demonlist.json', 'w') as f:
          json.dump(demonlist, f, indent=4)

    @commands.command(aliases=['rEMOVE', 'REMOVE', "Remove", "УДАЛИТЬ", "Удалить", "удалить", "уДАЛИТЬ"])
    @commands.has_role("РЕДАКТОР ДЕМОНЛИСТА")
    async def remove(self, ctx, index: int):
        await ctx.send(f"{dl[index][0]} удалён с демонлиста!")

        if index > 0 and index <= len(dl):
            dl.pop(index)

        demonlist["dl"] = dl
        with open('demonlist.json', 'w') as f:
          json.dump(demonlist, f, indent=4)

    @commands.command(aliases=['addvictor', 'плюсвиктор', "+виктор", "+ВИКТОР", "+Виктор"])
    @commands.has_role("РЕДАКТОР ДЕМОНЛИСТА")
    async def add_victor(self, ctx, index: int, victor: str, proof=""):
        if index > 0 and index <= len(dl):
            dl[index][2].append([victor, proof])
            await ctx.send(f'{victor} добавлен к викторам {dl[index][0]}!')
            with open('demonlist.txt', 'w') as f:
                f.write(str(dl))
        else:
            await ctx.send('Такой позиции не существует')
          
        demonlist["dl"] = dl
        with open('demonlist.json', 'w') as f:
          json.dump(demonlist, f, indent=4)

    @commands.command(aliases=['delvictor', '-виктор', "-Виктор", "-ВИКТОР"])
    @commands.has_role("РЕДАКТОР ДЕМОНЛИСТА")
    async def remove_victor(self, ctx, index: int, victor: str):
        if index > 0 and index <= len(dl):
            for i in range(len(dl[index][2])):
                print(i)
                if victor in dl[index][2][i]:
                    dl[index][2].pop(i)
                    await ctx.send(f"{victor} удалён с викторов {dl[index][0]}!")
                    demonlist["dl"] = dl
                    with open('demonlist.json', 'w') as f:
                      json.dump(demonlist, f, indent=4)
        else:
            await ctx.send('Такой позиции не существует')

    @commands.command(aliases=['+proof', "+PROOF", '+Proof', "+пруф", "+ПРУФ", "+Пруф", "+пруфы", "+ПРУФЫ", "+Пруфы",
                               "пруф", "ПРУФ", "Пруф"])
    @commands.has_role("РЕДАКТОР ДЕМОНЛИСТА")
    async def add_proof(self, ctx, index: int, victor: str, proof: str):
        if index > 0 and index <= len(dl):
            variable = 0
            for i in range(len(dl[index][2])):
                print(i)
                if victor in dl[index][2][i]:
                    dl[index][2][i][1] = proof
                    await ctx.send(f"Теперь пруф привязан к виктору уровня {dl[index][0]} - {victor}!")
                    demonlist["dl"] = dl
                    with open('demonlist.json', 'w') as f:
                      json.dump(demonlist, f, indent=4)
                else:
                    variable += 1
            if variable == len(dl[index][2]):
              await ctx.send("Такой игрок не найден!")
        else:
            await ctx.send('Такой позиции не существует!')

    @commands.command(aliases=['изменить', "ИЗМЕНИТЬ", "Изменить", 'EDIT', 'Edit'])
    @commands.has_role('РЕДАКТОР ДЕМОНЛИСТА')
    async def edit(self, ctx, index_one: int, index_two: int):
        if 0 < index_two <= len(dl) and 0 < index_one <= len(dl):
            editable = dl[index_one]
            dl.pop(index_one)
            dl.insert(index_two, editable)
            await ctx.send(f"{editable[0]} перенесён на позицию {index_two} с позиции {index_one}!")
            demonlist["dl"] = dl
            with open('demonlist.json', 'w') as f:
              json.dump(demonlist, f, indent=4)
        else:
            await ctx.send('Такой позиции не существует!')

    @commands.command(aliases=['длбан', "Длбан", "ДЛБАН", 'DLBAN', 'Dlban'])
    @commands.has_role('РЕДАКТОР ДЕМОНЛИСТА')
    async def dlban(self, ctx, player: str):
        for i in range(len(dl)):
            if dl[i][2] == 'Victors':
                continue
            for j in range(len(dl[i][2])):
                if player in dl[i][2][j][0]:
                    if len(dl[i][2]) == 1:
                        dl.pop(i)
                    else:
                        dl[i][2].pop(j)
        demonlist["dl"] = dl
        await ctx.send(f"{player} был удалён с демонлиста")
        with open('demonlist.json', 'w') as f:
          json.dump(demonlist, f, indent=4)

    @commands.command()
    @commands.has_role("РЕДАКТОР ДЕМОНЛИСТА")
    async def save(self, ctx):
      with open('demonlist_backup.json', 'w') as f:
          json.dump(demonlist, f, indent=4)

      await ctx.send("Файл сохранён")

    @commands.command()
    @commands.has_role("РЕДАКТОР ДЕМОНЛИСТА")
    async def load(self, ctx):
      global demonlist, dl
      with open('demonlist_backup.json', 'r') as f:
        demonlist = json.load(f)
      dl = demonlist["dl"]
      with open('demonlist.json', 'w') as f:
          json.dump(demonlist, f, indent=4)

      await ctx.send("Файл загружен")

    @commands.command(aliases=['длправила', "ДЛПРАВИЛА", "Длправила", "ДлПравила", "ДЛправила", "ДЛПравила", "длПРАВИЛА", "ДлПРАВИЛА",  "дЛПРАВИЛА"])
    async def dlrools(self, ctx):
      emojis = {e.name: str(e) for e in ctx.bot.emojis}
      await ctx.send(embed=discord.Embed(
        title="Правила демонлиста GMD | Общение",
        description=f''' 

  **1.1** В демонлист вы можете попасть только при наличии 10+ уровня;
        
  **1.2** Пруфы: Инсейн демоны и легче - по доверию, но пруфы лишними не будут. На экстрим демоны - видео с кликами. Но если вы по какой-то причине не смогли записать видеодоказательство вашего прохождения,  вы можете всё равно попасть в демонлист, если вы доверенный участник нашего сервера или если у вас есть пруф, на котором вы поставили +55% на пройденном уровне;
        
  **1.3** Если редактор демонлиста заподозрил что-либо неладное в пруфе прохождения - он в праве вас допросить, и в случае чего убрать ваши прохождения с демонлиста.
        
  **1.4** Если вы использовали различного рода сикрет веи и другие нечестные пути заполучить преимущество в сложности в уровне -  ваше прохождение не будет добавлено в демонлист

**Спасибо, что дочитал! Enjoy this delicious meal!** {emojis['GL']}
                     ''',
        colour=discord.Colour.purple()))


    @commands.command(aliases=["уровень", "УРОВЕНЬ", "Уровень", "уРОВЕНЬ"])
    async def level(self, ctx, *, name: str):
      check = 0
    
      for i in range(len(dl)):
        if name.lower() == dl[i][0].lower():
          check = 1
          position = i
          name = dl[i][0]
          author = dl[i][1]
          victors = ""
  
          for j in dl[i][2]:
            if j[1] == "":
              victors += f"{j[0]}\n"
            else:
              victors += f"[{j[0]}]({j[1]})\n "
  
          break

      if position > 100:
        points_count = 0
      else:
        points_count = points[position]
  
      if check == 0:
        await ctx.send("Уровень не найден")
      else:
        await ctx.send(
           embed=discord.Embed(
             title=f"{name}",
             description=f"""

             Позиция: **{position}**
             Название: **{name}**
             Автор: **{author}**
             Поинты: **{points_count}**

             Викторы:
             **{victors}**
             """,
             colour=discord.Colour.purple()
           ))

    @commands.command(aliases=["рівень", "РІВЕНЬ", "Рівень", "рІВЕНЬ"])
    async def livel(self, ctx, *, name: str):
      check = 0
    
      for i in range(len(dl)):
        if name.lower() == dl[i][0].lower():
          check = 1
          position = i
          name = dl[i][0]
          author = dl[i][1]
          victors = ""
  
          for j in dl[i][2]:
            if j[1] == "":
              victors += f"{j[0]}\n"
            else:
              victors += f"[{j[0]}]({j[1]})\n "
  
          break
  
      if check == 0:
        await ctx.send("Рівня не знайденр")
      else:
        await ctx.send(
           embed=discord.Embed(
             title=f"{name}",
             description=f"""

             Позиція: **{position}**
             Назва: **{name}**
             Автор: **{author}**

             Переможці:
             **{victors}**
             """,
             colour=discord.Colour.blue()
           ))


def setup(bot):
    bot.add_cog(Demonlist(bot))
