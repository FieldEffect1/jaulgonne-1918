"""
Génération des voix off pour Jaulgonne 1918
============================================
Génère 6 jalons × 2 langues = 12 fichiers MP3

Usage:
  pip install elevenlabs openai

  # Avec ElevenLabs (recommandé - meilleure qualité française)
  python generate_audio.py --api elevenlabs --key YOUR_API_KEY

  # Avec OpenAI TTS (alternative)
  python generate_audio.py --api openai --key YOUR_API_KEY

Les fichiers sont créés dans:
  audio/fr/jalon_0.mp3 … jalon_5.mp3
  audio/en/jalon_0.mp3 … jalon_5.mp3
"""

import os
import sys
import argparse
from pathlib import Path

# ── TEXTES DE NARRATION ──────────────────────────────────────────────────────

NARRATIONS = [
    {
        "id": 0,
        "fr": (
            "27 mai, 4 juin 1918. "
            "Le 30 mai 1918 au soir, les soldats allemands de la vingt-huitième division "
            "atteignent les rives de la Marne à Jaulgonne. "
            "Soixante kilomètres les séparent de Paris. "
            "Dans les nuits du 31 mai au 2 juin, un bataillon de la trente-sixième division "
            "tente le passage. "
            "Face à eux, des poilus du Bataillon Sagnières du 47e Régiment d'Infanterie "
            "tiennent la Ferme des Franquets sur les hauteurs. "
            "Ceux du Bataillon Taureau s'accrochent aux pentes entre la ferme et la forêt. "
            "Le 2 juin, une contre-attaque franco-américaine rejette les envahisseurs. "
            "Le pont flottant est détruit. Cent prisonniers. "
            "Jaulgonne est sauvé… pour l'instant."
        ),
        "en": (
            "May 27th to June 4th, 1918. "
            "On the evening of May 30th, 1918, German soldiers of the 28th Division "
            "reach the banks of the Marne River at Jaulgonne. "
            "Just 37 miles separate them from Paris. "
            "During the nights of May 31st to June 2nd, a battalion of the 36th Division "
            "attempts the crossing. "
            "Facing them, French soldiers of the Sagnières Battalion of the 47th Infantry Regiment "
            "hold the Ferme des Franquets on the heights. "
            "The Taureau Battalion clings to the slopes between the farm and the forest. "
            "On June 2nd, a Franco-American counter-attack throws the invaders back. "
            "The pontoon bridge is destroyed. One hundred prisoners taken. "
            "Jaulgonne is saved… for now."
        )
    },
    {
        "id": 1,
        "fr": (
            "15 au 17 juillet 1918. "
            "Dans la nuit du 14 au 15 juillet, un déluge d'acier et de gaz s'abat sur les positions alliées. "
            "Les Allemands lancent le Friedensturm — l'assaut de la paix. "
            "Phosgène, ypérite, obus à gaz Croix Bleue : "
            "des nuages mortels enveloppent Jaulgonne et la Forêt de Ris. "
            "L'aviation alliée effectue des bombardements massifs sur la Marne. "
            "Puis des ponts flottants de huit à dix mètres sont jetés sur le fleuve. "
            "Dès sept heures trente-cinq, la 73e Division d'Infanterie française contre-attaque "
            "dans la boucle de Jaulgonne, en direction de Mézy. "
            "Les soldats américains du 38e Régiment d'Infanterie — "
            "des hommes ordinaires venus de l'Ohio, du Michigan, de Pennsylvanie — "
            "se retrouvent encerclés en position de fer à cheval à Mézy. "
            "Pendant quatorze heures, sans ordre de retraite, dans les gaz et sous les obus, "
            "ils résistent seuls à six régiments allemands. "
            "On les appellera les Rochers de la Marne."
        ),
        "en": (
            "July 15th to 17th, 1918. "
            "In the night of July 14th to 15th, a deluge of steel and gas falls upon Allied positions. "
            "The Germans launch the Friedensturm — the Peace Assault. "
            "Phosgene, mustard gas, Blue Cross shells: "
            "deadly clouds shroud Jaulgonne and the Forêt de Ris forest. "
            "Allied aircraft carry out massive bombing raids on the Marne. "
            "Then pontoon bridges eight to ten meters wide are thrown across the river. "
            "At 7:35 in the morning, the French 73rd Infantry Division counter-attacks "
            "in the Jaulgonne Bend, toward Mézy. "
            "American soldiers of the 38th Infantry Regiment — "
            "ordinary men from Ohio, Michigan, Pennsylvania — "
            "find themselves surrounded in a horseshoe position at Mézy. "
            "For fourteen hours, without orders to retreat, through gas and shellfire, "
            "they hold alone against six German regiments. "
            "They will be called the Rock of the Marne."
        )
    },
    {
        "id": 2,
        "fr": (
            "18 juillet 1918. "
            "À l'aube, sans barrage d'artillerie préparatoire — la surprise totale — "
            "vingt-quatre divisions alliées et trois cent cinquante chars s'élancent. "
            "Le général Mangin attaque. "
            "Des soldats français et américains avancent côte à côte "
            "à travers les bois, les blés mûrs, les vignes de la Marne. "
            "En un seul jour, les lignes allemandes reculent de trois à huit kilomètres. "
            "Ce jour marque le tournant définitif de la Grande Guerre : "
            "pour la première fois depuis 1914, l'armée allemande est contrainte de reculer "
            "sur tout le front occidental."
        ),
        "en": (
            "July 18th, 1918. "
            "At dawn, with no preparatory artillery barrage — complete surprise — "
            "twenty-four Allied divisions and 350 tanks surge forward. "
            "General Mangin attacks. "
            "French and American soldiers advance side by side "
            "through the woods, the ripe wheat fields, the Marne vineyards. "
            "In a single day, German lines fall back three to five miles. "
            "This day marks the turning point of the Great War: "
            "for the first time since 1914, the German army is forced back "
            "along the entire Western Front."
        )
    },
    {
        "id": 3,
        "fr": (
            "22 au 24 juillet 1918. "
            "Les soldats du 38e Régiment d'Infanterie américain traversent la Marne "
            "et montent à l'assaut de Jaulgonne. "
            "Dans le même secteur, la 28e Division américaine combat dans les forêts au nord. "
            "D'abord cloués au sol par les mitrailleuses et l'artillerie allemandes, "
            "les hommes du 38e percent finalement les défenses. "
            "Le 22 juillet, Jaulgonne est libéré. Mont-Saint-Père et Chartèves tombent à leur tour. "
            "Les combats pour la Ferme des Franquets se prolongent les 22, 23 et 24 juillet : "
            "la ferme n'est définitivement reprise que le 24. "
            "Près de trois cents soldats ennemis sont faits prisonniers dans le secteur. "
            "Pour ces hommes qui avaient tenu la Marne le 15 juillet, "
            "c'est la victoire."
        ),
        "en": (
            "July 22nd to 24th, 1918. "
            "Soldiers of the 38th US Infantry Regiment cross the Marne "
            "and assault Jaulgonne. "
            "In the same sector, the 28th US Division fights through the forests to the north. "
            "Initially pinned down by German machine guns and artillery, "
            "the men of the 38th finally break through. "
            "On July 22nd, Jaulgonne is liberated. Mont-Saint-Père and Chartèves fall in turn. "
            "Fighting for the Ferme des Franquets continues on July 22nd, 23rd, and 24th: "
            "the farm is not finally secured until July 24th. "
            "Nearly three hundred enemy soldiers are taken prisoner in the sector. "
            "For the men who held the Marne on July 15th, "
            "this is their victory."
        )
    },
    {
        "id": 4,
        "fr": (
            "Été — automne 1918. "
            "Libéré, Jaulgonne est anéanti. "
            "Les maisons éventrées, l'église dévastée, les ponts détruits, "
            "les quais de la Marne jonchés de débris. "
            "En trois semaines de contre-offensive, deux cents villages ont été libérés, "
            "trente-cinq mille prisonniers capturés, sept cents canons pris. "
            "L'armée allemande ne lancera plus jamais d'offensive de cette ampleur. "
            "La Grande Guerre touche à sa fin. "
            "Mais pour les habitants de Jaulgonne, la vie n'existe plus."
        ),
        "en": (
            "Summer through autumn, 1918. "
            "Liberated, Jaulgonne lies in ruins. "
            "Houses gutted, the church devastated, bridges destroyed, "
            "the Marne quays strewn with debris. "
            "In three weeks of counter-offensive, 200 villages were liberated, "
            "35,000 prisoners captured, 700 guns taken. "
            "The German army will never again launch an offensive of this scale. "
            "The Great War nears its end. "
            "But for the people of Jaulgonne, life no longer exists."
        )
    },
    {
        "id": 5,
        "fr": (
            "1919, et après. "
            "Ils avaient des noms inconnus. "
            "Ils portaient leur numéro de régiment comme seul identifiant. "
            "Certains venaient de Paris, de Lyon, de Bretagne. "
            "D'autres de New York, de Chicago, de fermes du Middle West. "
            "Ils avaient vingt ans, peut-être. Ou trente. "
            "Certains ont survécu. Beaucoup non. "
            "La loi du 17 avril 1919 a permis de rebâtir les pierres. "
            "Mais aucune loi ne peut rebâtir un homme. "
            "Le mémorial américain d'Aisne-Marne à Château-Thierry se dresse pour eux. "
            "Ce site se dresse pour eux. "
            "Pour que nul ne soit oublié."
        ),
        "en": (
            "1919, and after. "
            "They had no famous names. "
            "They bore their regiment number as their only identifier. "
            "Some came from Paris, Lyon, Brittany. "
            "Others from New York, Chicago, farms in the Midwest. "
            "They were perhaps twenty years old. Or thirty. "
            "Some survived. Many did not. "
            "The law of April 17th, 1919 allowed the stones to be rebuilt. "
            "But no law can rebuild a man. "
            "The American Aisne-Marne Memorial at Château-Thierry stands for them. "
            "This site stands for them. "
            "So that none are forgotten."
        )
    }
]


def generate_with_elevenlabs(api_key: str, output_dir: Path):
    """Generate audio using ElevenLabs API."""
    try:
        from elevenlabs import ElevenLabs, VoiceSettings
    except ImportError:
        print("ERROR: pip install elevenlabs")
        sys.exit(1)

    client = ElevenLabs(api_key=api_key)

    # Voice IDs: use multilingual voices for best FR quality
    # These are public ElevenLabs voices — change if preferred
    VOICES = {
        "fr": "pNInz6obpgDQGcFmaJgB",  # Adam (multilingual) — change as needed
        "en": "21m00Tcm4TlvDq8ikWAM",  # Rachel
    }

    for lang, voice_id in VOICES.items():
        lang_dir = output_dir / lang
        lang_dir.mkdir(parents=True, exist_ok=True)
        for jalon in NARRATIONS:
            out_path = lang_dir / f"jalon_{jalon['id']}.mp3"
            if out_path.exists():
                print(f"  [skip] {out_path} already exists")
                continue
            text = jalon[lang]
            print(f"  Generating [{lang}] jalon_{jalon['id']}...", end=" ", flush=True)
            audio = client.text_to_speech.convert(
                voice_id=voice_id,
                text=text,
                model_id="eleven_multilingual_v2",
                voice_settings=VoiceSettings(
                    stability=0.5,
                    similarity_boost=0.8,
                    style=0.3,
                    use_speaker_boost=True,
                )
            )
            with open(out_path, "wb") as f:
                for chunk in audio:
                    f.write(chunk)
            print(f"OK ({out_path})")


def generate_with_openai(api_key: str, output_dir: Path):
    """Generate audio using OpenAI TTS API."""
    try:
        from openai import OpenAI
    except ImportError:
        print("ERROR: pip install openai")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    VOICES = {
        "fr": "nova",   # Works for French, neutral tone
        "en": "shimmer" # Warm narrative voice for English
    }

    for lang, voice in VOICES.items():
        lang_dir = output_dir / lang
        lang_dir.mkdir(parents=True, exist_ok=True)
        for jalon in NARRATIONS:
            out_path = lang_dir / f"jalon_{jalon['id']}.mp3"
            if out_path.exists():
                print(f"  [skip] {out_path} already exists")
                continue
            text = jalon[lang]
            print(f"  Generating [{lang}] jalon_{jalon['id']}...", end=" ", flush=True)
            response = client.audio.speech.create(
                model="tts-1-hd",
                voice=voice,
                input=text,
                response_format="mp3"
            )
            response.stream_to_file(str(out_path))
            print(f"OK ({out_path})")


def main():
    parser = argparse.ArgumentParser(description="Génération voix off Jaulgonne 1918")
    parser.add_argument("--api", choices=["elevenlabs", "openai"], default="elevenlabs",
                        help="API TTS à utiliser (défaut: elevenlabs)")
    parser.add_argument("--key", required=True, help="Clé API")
    parser.add_argument("--output", default="audio", help="Dossier de sortie (défaut: audio/)")
    args = parser.parse_args()

    output_dir = Path(args.output)
    print(f"\nJaulgonne 1918 — Génération voix off")
    print(f"API    : {args.api}")
    print(f"Output : {output_dir}/fr/ et {output_dir}/en/")
    print(f"Jalons : {len(NARRATIONS)} × 2 langues = {len(NARRATIONS)*2} fichiers MP3\n")

    if args.api == "elevenlabs":
        generate_with_elevenlabs(args.key, output_dir)
    else:
        generate_with_openai(args.key, output_dir)

    print(f"\nTerminé. Ouvrir index.html dans un navigateur pour tester.")


if __name__ == "__main__":
    main()
