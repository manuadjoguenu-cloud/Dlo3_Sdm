from django.core.management.base import BaseCommand
from site_dlo3.models import Communaute, Activite


COMMUNAUTES = [
    dict(slug="adidogome", type="Paroisse", vocable="Marie Mère du Rédempteur", lieu="Adidogomé",
         cure="RP Michel ESSEH", responsable_nom="Fr Simon", responsable_tel="+22879925369",
         latitude=6.183107023757032, longitude=1.1684021510975247),
    dict(slug="awatame", type="Sanctuaire", vocable="Saint Sacrement", lieu="Awatamé",
         recteur="RP Paul AMOUZOU", responsable_nom="", responsable_tel="",
         latitude=6.174395025466483, longitude=1.1738167934268362),
    dict(slug="amandahome", type="Paroisse", vocable="Jésus Miséricordieux", lieu="Amandahomé",
         cure="RP Paul AMAGLO", responsable_nom="Fr Victor", responsable_tel="",
         latitude=6.491640034423829, longitude=1.2890732241119904),
    dict(slug="apedokoe", type="Paroisse", vocable="Sancta Maria Regina Pacis", lieu="Apédokoé",
         cure="RP Georges GBAFA", responsable_nom="Fr Emmanuel ADJOGUENU", responsable_tel="+22891427225",
         latitude=6.2044725857032486, longitude=1.1414432106153627),
    dict(slug="yokoe", type="Paroisse", vocable="Saint Jean-Baptiste", lieu="Yokoé",
         cure="RP Johannes AZIABLI", responsable_nom="Fr Léonce", responsable_tel="+22897625756",
         latitude=6.178151991687143, longitude=1.14479208177982),
    dict(slug="wonyome", type="Paroisse", vocable="Notre Dame du Sacré-Cœur", lieu="Wonyomé",
         cure="RP Placide TEFE", responsable_nom="Fr Aimé-césaire", responsable_tel="+22893812395",
         latitude=6.191473909451884, longitude=1.149823617498672),
    dict(slug="logote", type="Paroisse", vocable="Christ-Ressuscité", lieu="Sagbado-Logoté",
         cure="RP Victor ATSOUTSE", responsable_nom="Fr Christophe", responsable_tel="+22892738605",
         latitude=6.194324523091906, longitude=1.1278396694464115),
    dict(slug="segbe", type="Paroisse", vocable="Notre Dame du Perpétuel Secours", lieu="Ségbé",
         cure="RP Gaston AMOUZOU", responsable_nom="Fr Nicodème EKLOU", responsable_tel="+22896554334",
         latitude=6.193893623448216, longitude=1.1127690106152526),
    dict(slug="akato", type="Paroisse", vocable="Saint Joseph", lieu="Akato-viépé",
         cure="RP Augstin SOEDJEDE", responsable_nom="Fr Michel", responsable_tel="+22873047754",
         latitude=6.186597782691736, longitude=1.1034992280174154),
    dict(slug="agblegan", type="Paroisse", vocable="Notre Dame de la Miséricorde", lieu="Agblégan",
         cure="RP Romain NAYO", responsable_nom="Fr Modeste", responsable_tel="+22891004775",
         latitude=6.173978859563276, longitude=1.1589029971209968),
    dict(slug="kohe", type="Paroisse", vocable="Notre Dame de la Médaille Miraculeuse", lieu="Kohé",
         cure="RP David SOSSOU", responsable_nom="Emile", responsable_tel="+22898802832",
         latitude=6.225960789621908, longitude=1.1381320559419392),
    dict(slug="zossime", type="Paroisse", vocable="Sainte Rita", lieu="Zossimé",
         cure="RP Philippe Jacques GAMISSO", responsable_nom="", responsable_tel="",
         latitude=6.231464310002285, longitude=1.1549420510979174),
    dict(slug="balissime", type="Quasi-Paroisse", vocable="Saint-Esprit", lieu="Balissimé",
         cure="RP Jean AMEGNEKOU", responsable_nom="Fr Prosper", responsable_tel="+22896170504",
         latitude=6.203667821730847, longitude=1.1208339191883854),
    dict(slug="agokpanou", type="Quasi-Paroisse", vocable="Saint Michel Archange", lieu="Klémé-Agokpanou",
         cure="RP Dominique ASSIGNON", responsable_nom="", responsable_tel="",
         latitude=6.213570978349144, longitude=1.1106053412977992),
    dict(slug="logogome", type="Quasi-Paroisse", vocable="Virgo Potens", lieu="Logogomé",
         cure="RP Florentin TOKOU", responsable_nom="Fr Sylvanus", responsable_tel="+22891426446",
         latitude=6.213838020199823, longitude=1.1481544817801368),
    dict(slug="agotile", type="Quasi-Paroisse", vocable="Notre Dame du Rosaire", lieu="Sagbado-Agotimé",
         cure="RP Marie-Athanase ATTIGNON", responsable_nom="Fr Daniel", responsable_tel="+22896859302",
         latitude=6.187991388700796, longitude=1.136765771979967),
    dict(slug="soviepe", type="Quasi-Paroisse", vocable="Saint Daniel Comboni", lieu="Avédji-Anyigbé-Soviépé",
         cure="RP Saturnin POGNON", responsable_nom="", responsable_tel="",
         latitude=6.1715729938158015, longitude=1.1787633492503051),
    dict(slug="glinkomegan", type="Station secondaire", vocable="Notre Dame de Lourdes", lieu="Gblinkomégan",
         cure="RP Michel ESSEH", responsable_nom="Pacôme", responsable_tel="+22872120852",
         latitude=6.182168522700481, longitude=1.1576424224493604),
    dict(slug="wessome", type="Station secondaire", vocable="Saint Christophe", lieu="Wessomé",
         cure="RP Michel ESSEH", responsable_nom="", responsable_tel="",
         latitude=6.198005285656681, longitude=1.1659753241094069),
    dict(slug="lankouvi1", type="Station secondaire", vocable="Marie Porte du Ciel", lieu="Lankouvi",
         cure="RP Michel ESSEH", responsable_nom="Fr Raphaël", responsable_tel="+22892599183",
         latitude=6.180276255352774, longitude=1.125107852944531),
    dict(slug="lankouvi2", type="Station secondaire", vocable="Saint Charles Lwanga", lieu="Lankouvi-Zogbédji",
         cure="RP Michel ESSEH", responsable_nom="", responsable_tel="",
         latitude=6.170647993928604, longitude=1.1164614836268192),
    dict(slug="avoeme", type="Station secondaire", vocable="Jésus Miséricordieux", lieu="Akato-Avoémé",
         cure="RP Michel ESSEH", responsable_nom="", responsable_tel="",
         latitude=6.201115833198081, longitude=1.0871062208275464),
    dict(slug="djigbe", type="Station secondaire", vocable="Saint Justin", lieu="Klémé-Djigbé",
         cure="RP Michel ESSEH", responsable_nom="", responsable_tel="",
         latitude=6.21118238649098, longitude=1.0963573241095215),
]

ACTIVITES = [
    dict(slug="meet", icone="🤝", titre="Réunion des Responsables", ordre=1,
         accroche="Coordination entre paroisses",
         description="Cette réunion rassemble les responsables des différentes paroisses du doyenné. "
                      "Elle est l'occasion de réfléchir ensemble au bon fonctionnement du DLO3 et d'organiser "
                      "les prochaines activités communes aux servants de Messe. Elle se tient une fois par mois, "
                      "avec possibilité de réunions extraordinaires selon les besoins. Chaque communauté doit y "
                      "être représentée par au moins un responsable de base."),
    dict(slug="recollection", icone="🙏", titre="Récollection", ordre=2,
         accroche="Un temps de silence et de prière",
         description="Deux temps de récollection sont réservés chaque année : pendant le Carême et pendant "
                      "l'Avent. Ces moments de prière et de recueillement permettent aux servants de Messe "
                      "d'approfondir leur foi. Le lieu est choisi lors des réunions des responsables. "
                      "L'organisation revient au bureau décanal, avec l'appui d'un accompagnateur spirituel "
                      "(prêtre, diacre, abbé ou aîné)."),
    dict(slug="camp", icone="🏕️", titre="Camp de formation", ordre=3,
         accroche="Apprentissage et vie communautaire",
         description="Le camp de formation se déroule sur une semaine, pendant les vacances. Il alterne ateliers "
                      "pratiques, enseignements bibliques et temps de divertissement, rythmés par la prière et "
                      "les repas pris en communauté. Encadrés par les responsables et un accompagnateur spirituel, "
                      "les servants de Messe de toutes les paroisses du doyenné s'y retrouvent — un moment fort "
                      "de cohésion et de vie fraternelle, au-delà de la formation elle-même. Le programme, comme "
                      "le lieu du camp, est établi lors de la réunion des responsables."),
    dict(slug="amitie", icone="🎉", titre="Journée d'amitié", ordre=4,
         accroche="Le plus souvent le 28 décembre, fête des Saints Innocents",
         description="La Journée d'amitié se tient le plus souvent le 28 décembre, jour de la fête des Saints "
                      "Innocents, traditionnellement associée aux servants de Messe. Elle rassemble les servants "
                      "de toutes les paroisses du doyenné dans un esprit de partage et de convivialité."),
]


class Command(BaseCommand):
    help = "Charge les communautés et activités déjà renseignées dans les pages statiques du site."

    def handle(self, *args, **options):
        crees_c = 0
        for data in COMMUNAUTES:
            _, cree = Communaute.objects.update_or_create(slug=data["slug"], defaults=data)
            crees_c += cree

        crees_a = 0
        for data in ACTIVITES:
            _, cree = Activite.objects.update_or_create(slug=data["slug"], defaults=data)
            crees_a += cree

        self.stdout.write(self.style.SUCCESS(
            f"{len(COMMUNAUTES)} communautés et {len(ACTIVITES)} activités chargées "
            f"({crees_c} nouvelles communautés, {crees_a} nouvelles activités)."
        ))
