okayu = '''Ever on and on I continue circling
With nothing but my hate in a carousel of agony
Till slowly I forget and my heart starts vanishing

And suddenly I see that I can't break free--I'm
Slipping through the cracks of a dark eternity
With nothing but my pain and the paralyzing agony

To tell me who I am, who I was
Uncertainty enveloping my mind
Till I can't break free, and

Maybe it's a dream; maybe nothing else is real
But it wouldn't mean a thing if I told you how I feel
So I'm tired of the pain, of the misery inside
And I wish that I could live feeling nothing but the night
You can tell me what to say; you can tell me where to go
But I doubt that I would care, and my heart would never know

If I make another move there'll be no more turning back
Because everything will change, and it all will fade to black
Will tomorrow ever come? Will I make it through the night?

Will there ever be a place for the broken in the light?
Am I hurting? Am I sad? Should I stay, or should I go?
I've forgotten how to tell. Did I ever even know?

Can I take another step? I've done everything I can
All the people that I see I will never understand
If I find a way to change, if I step into the light

Then I'll never be the same, and it all will fade to white

Ever on and on I continue circling

With nothing but my hate in a carousel of agony
Till slowly I forget and my heart starts vanishing
And suddenly I see that I can't break free--I'm

Slipping through the cracks of a dark eternity
With nothing but my pain and the paralyzing agony
To tell me who I am, who I was

Uncertainty enveloping my mind
Till I can't break free, and
Maybe it's a dream; maybe nothing else is real

But it wouldn't mean a thing if I told you how I feel
So I'm tired of the pain, of the misery inside
And I wish that I could live feeling nothing but the night
You can tell me what to say; you can tell me where to go
But I doubt that I would care, and my heart would never know
If I make another move there'll be no more turning back

Because everything will change, and it all will fade to black
If I make another move, if I take another step
Then it all would fall apart. There'd be nothing of me left

If I'm crying in the wind, if I'm crying in the night
Will there ever be a way? Will my heart return to white?
Can you tell me who you are? Can you tell me where I am?I've forgotten how to see; I've forgotten if I can

If I opened up my eyes there'd be no more going back
'Cause I'd throw it all away, and it all would fade to black '''

print(len(okayu))

in1 = input('what do you wish to replace?')
in2 = input('what do you wish to replace this time?')
in3 = input('And what do you wish to replace it with?')
in4 = input('And what do you wish to replace it with this time?')
okayu1 = okayu.lower().replace(in1, in3)
okayu2 = okayu1.replace(in2, in4)
okayu3 = okayu2.splitlines()

for line in okayu3:
    print(line)