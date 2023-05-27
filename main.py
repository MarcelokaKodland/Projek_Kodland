import discord
import random
import asyncio


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        
if message.content.startswith('$help'):
            await message.channel.send('Aku bot. Aku bisa beragai hal. ketik "$pass", maka aku akan membuatkanmu password yang kuat. Ketik "$coin", maka kita akan bermain lempar koin. Ketik "$emoji", maka aku akan mengeluarkan emoji acak. Ketik "$guess", kita akan bermain tebak angka. Ketik "$math_exercise", maka kita akan berlatih matematika')
        
        if message.content.startswith('$hello'):
            await message.channel.send('Saya! Saya bot!')

        if message.content.startswith('$pass'):
            await message.channel.send('Mau password berapa digit?')
            def is_correct(m):
                return m.author == message.author and m.content.isdigit()
            try :
                digit = await self.wait_for('message', check=is_correct, timeout=700.0)
            except asyncio.TimeoutError :
                return await message.channel.send('Maaf, kamu kelamaan. Masukin perintahnya lagi')
            elements = "+-/*!&$#?=@<>ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            password = ""
            
            for i in range(int(digit.content)):
                password += random.choice(elements)

            await message.channel.send(password)
        
        if message.content.startswith('$coin'):
            flip = random.randint(0, 1)
            answer = ""

            if flip == 0:
                answer = "HEADS"
            else:
                answer = "TAILS"
        
            await message.channel.send(answer)

        if message.content.startswith('$emoji'):
            emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
            await message.channel.send(random.choice(emodji))

        if message.content.startswith('$guess'):
            await message.channel.send('Tebak angka dari 1 sampai 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sorry, you took too long it was {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('WOW! Kamu benar, lho! Kamu cenayang ya???')
            else:
                await message.channel.send(f'Kurang beruntung. Jawabannya {answer}.')

        if message.content.startswith('$math_exercise'):
            await message.channel.send('Pilih mode (penjumlahan, perkalian)')
            try :
                mode = await self.wait_for('message', timeout=700.0)
            except asyncio.TimeoutError :
                return await message.channel.send('Maaf, kamu kelamaan. Masukin perintahnya lagi')
        
            if mode.content == 'penjumlahan':
                jawaban = 0

                def is_correct(m):
                    return m.author == message.author and m.content.isdigit()
                
                await message.channel.send('Mau penjumlahan berapa angka?')
                try: 
                    jumlah = await self.wait_for('message', check=is_correct, timeout=700.0)
                except asyncio.TimeoutError :
                    return await message.channel.send('Maaf, kamu kelamaan. Masukin perintahnnya lagi')

                await message.channel.send('Pilih kisaran angka paling kecil')
                try: 
                    kecil = await self.wait_for('message', check=is_correct, timeout=700.0)
                except asyncio.TimeoutError :
                    return await message.channel.send('Maaf, kamu kelamaan. Masukin perintahnnya lagi')
                
                await message.channel.send('Pilih kisaran angka paling besar')
                try: 
                    besar = await self.wait_for('message', check=is_correct, timeout=700.0)
                except asyncio.TimeoutError :
                    return await message.channel.send('Maaf, kamu kelamaan. Masukin perintahnnya lagi')
                
                for i in range(int(jumlah.content)):
                    angka = random.randint(int(kecil.content),int(besar.content))
                    jawaban += angka
                    await message.channel.send(f'{angka} ditambah')

                await message.channel.send('adalah')
                try: 
                    jwbn = await self.wait_for('message', check=is_correct, timeout=700.0)
                except asyncio.TimeoutError :
                    return await message.channel.send('Maaf, kamu kelamaan. Masukin perintahnnya lagi')
                
                if int(jwbn.content) == jawaban :
                    await message.channel.send('BRAVO! KAMU BENAR')
                else:
                    await message.channel.send(f'Oops. Jawabannya {jawaban}. Ayo coba lagi')

            if mode.content == 'perkalian':
                jawaban = 1
        
                def is_correct(m):
                    return m.author == message.author and m.content.isdigit()
                
                await message.channel.send('Mau perkalian berapa angka?')
                try: 
                    jumlah = await self.wait_for('message', check=is_correct, timeout=700.0)
                except asyncio.TimeoutError :
                    return await message.channel.send('Maaf, kamu kelamaan. Masukin perintahnnya lagi')

                await message.channel.send('Pilih kisaran angka paling kecil')
                try: 
                    kecil = await self.wait_for('message', check=is_correct, timeout=700.0)
                except asyncio.TimeoutError :
                    return await message.channel.send('Maaf, kamu kelamaan. Masukin perintahnnya lagi')
                
                await message.channel.send('Pilih kisaran angka paling besar')
                try: 
                    besar = await self.wait_for('message', check=is_correct, timeout=700.0)
                except asyncio.TimeoutError :
                    return await message.channel.send('Maaf, kamu kelamaan. Masukin perintahnnya lagi')

                for i in range(int(jumlah.content)):
                    angka = random.randint(int(kecil.content),int(besar.content))
                    jawaban *= angka
                    await message.channel.send(f'{angka} dikali')

                await message.channel.send('adalah')
                try: 
                    jwbn = await self.wait_for('message', check=is_correct, timeout=700.0)
                except asyncio.TimeoutError :
                    return await message.channel.send('Maaf, kamu kelamaan. Masukin perintahnnya lagi')
                
                if int(jwbn.content) == jawaban :
                    await message.channel.send('BRAVO! KAMU BENAR')
                else:
                    await message.channel.send(f'Oops. Jawabannya {jawaban}. Ayo coba lagi')



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('ISI TOKEN DI SINI')
