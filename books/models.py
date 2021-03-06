# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import MySQLdb
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from tilt.scrapy import modify_nocheck


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()


class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16)
    permission = models.IntegerField(default=1)


class Ltecell(models.Model):
    cellname = models.CharField(max_length=100)
    cellid1 = models.CharField(max_length=20)
    cellomcname = models.CharField(max_length=100)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    villages = models.CharField(max_length=20)
    enodebid = models.CharField(max_length=10)
    cellid2 = models.CharField(max_length=10)
    sector = models.CharField(max_length=50)
    eutranCellid = models.CharField(max_length=50)
    factory = models.CharField(max_length=10)
    villagestypes = models.CharField(max_length=10)
    MR = models.CharField(max_length=10)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    antennaid = models.CharField(max_length=255)
    antennanum = models.CharField(max_length=50)
    worktypes = models.CharField(max_length=5)
    cp = models.CharField(max_length=10)
    subframe = models.CharField(max_length=10)
    specificsubframe = models.CharField(max_length=10)
    remoterru = models.CharField(max_length=20)
    upfpoint = models.CharField(max_length=50)
    downfpoint = models.CharField(max_length=50)
    pci = models.CharField(max_length=50)
    pcilist = models.CharField(max_length=50)
    cellmaxpower = models.CharField(max_length=50)
    rspower = models.CharField(max_length=50)
    atypepower1 = models.CharField(max_length=20)
    btypepower1 = models.CharField(max_length=10)
    atypepower2 = models.CharField(max_length=50)
    btypepower2 = models.CharField(max_length=10)
    bcchpower = models.CharField(max_length=50)
    maxpower = models.CharField(max_length=50)
    tac = models.CharField(max_length=10)
    taclist = models.CharField(max_length=10)
    operation = models.CharField(max_length=20)
    coveragetypes = models.CharField(max_length=20)
    coveragerange = models.CharField(max_length=20)
    plmn = models.CharField(max_length=20)
    mbms = models.CharField(max_length=10)
    band = models.CharField(max_length=10)
    centerfrequency = models.CharField(max_length=10)
    bandwidth = models.CharField(max_length=10)
    downCyclicPrefix = models.CharField(max_length=20)
    upCyclicPrefix = models.CharField(max_length=20)
    upbandwidth = models.CharField(max_length=10)
    downbandwidth = models.CharField(max_length=10)
    astat = models.CharField(max_length=10)
    hs = models.CharField(max_length=10)
    txrxmod = models.CharField(max_length=20)
    worktypes1 = models.CharField(max_length=20)
    leadingformat = models.CharField(max_length=20)
    isblocking = models.CharField(max_length=10)
    boundarycell = models.CharField(max_length=10)
    boundaryname = models.CharField(max_length=10)
    csbf = models.CharField(max_length=10)
    hs2 = models.CharField(max_length=10)
    istelecom = models.CharField(max_length=10)
    build = models.CharField(max_length=10)
    sharingmode = models.CharField(max_length=10)
    isca = models.CharField(max_length=10)
    catypes = models.CharField(max_length=10)
    catypeassociation = models.CharField(max_length=10)
    camaincellid = models.CharField(max_length=20)
    customize1 = models.CharField(max_length=50)
    customize2 = models.CharField(max_length=50)
    customize3 = models.CharField(max_length=50)
    customize4 = models.CharField(max_length=50)
    customize5 = models.CharField(max_length=50)
    customize6 = models.CharField(max_length=50)
    customize7 = models.CharField(max_length=50)
    customize8 = models.CharField(max_length=50)
    customize9 = models.CharField(max_length=50)
    customize10 = models.CharField(max_length=50)

    def init1(self, *args):
        # super(Ltecell, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.cellname = args[0]
                self.cellid1 = args[1]
                self.cellomcname = args[2]
                self.province = args[3]
                self.city = args[4]
                self.district = args[5]
                self.villages = args[6]
                self.enodebid = args[7]
                self.cellid2 = args[8]
                self.sector = args[9]
                self.eutranCellid = args[10]
                self.factory = args[11]
                self.villagestypes = args[12]
                self.MR = args[13]
                self.lon = args[14]
                self.lat = args[15]
                self.antennaid = args[16]
                self.antennanum = args[17]
                self.worktypes = args[18]
                self.cp = args[19]
                self.subframe = args[20]
                self.specificsubframe = args[21]
                self.remoterru = args[22]
                self.upfpoint = args[23]
                self.downfpoint = args[24]
                self.pci = args[25]
                self.pcilist = args[26]
                self.cellmaxpower = args[27]
                self.rspower = args[28]
                self.atypepower1 = args[29]
                self.btypepower1 = args[30]
                self.atypepower2 = args[31]
                self.btypepower2 = args[32]
                self.bcchpower = args[33]
                self.maxpower = args[34]
                self.tac = args[35]
                self.taclist = args[36]
                self.operation = args[37]
                self.coveragetypes = args[38]
                self.coveragerange = args[39]
                self.plmn = args[40]
                self.mbms = args[41]
                self.band = args[42]
                self.centerfrequency = args[43]
                self.bandwidth = args[44]
                self.downCyclicPrefix = args[45]
                self.upCyclicPrefix = args[46]
                self.upbandwidth = args[47]
                self.downbandwidth = args[48]
                self.astat = args[49]
                self.hs = args[50]
                self.txrxmod = args[51]
                self.worktypes1 = args[52]
                self.leadingformat = args[53]
                self.isblocking = args[54]
                self.boundarycell = args[55]
                self.boundaryname = args[56]
                self.csbf = args[57]
                self.hs2 = args[58]
                self.istelecom = args[59]
                self.build = args[60]
                self.sharingmode = args[61]
                self.isca = args[62]
                self.catypes = args[63]
                self.catypeassociation = args[64]
                self.camaincellid = args[65]
                self.customize1 = args[66]
                self.customize2 = args[67]
                self.customize3 = args[68]
                self.customize4 = args[69]
                self.customize5 = args[70]
                self.customize6 = args[71]
                self.customize7 = args[72]
                self.customize8 = args[73]
                self.customize9 = args[74]
                self.customize10 = args[75]
        return self

    def syn(self):
        connect_dict = {
            'host': '127.0.0.1',
            'user': 'root',
            'passwd': '123456',
            'port': 3306,
            'db': 'lwl224',
            'use_unicode': 'True',
            'charset': 'utf8'
        }
        conn = MySQLdb.connect(**connect_dict)
        cursor = conn.cursor()
        sql = "SELECT * FROM books_rru WHERE   cellid1 =" + self.cellid1 + "   ORDER BY physicalstationid DESC"
        n = cursor.execute(sql)
        para_dict = {'timestamp': '1511059747000', 'objectTypeId': 'L00862', 'complaintId': 'null',
                     'objectId': '110.110.698043.3', 'cell_4g': '', 'cell_3g': '', 'cell_2g': '', 'test': '',
                     'RRU_ID': '110.698043.3', 'LC_NAME': 'GX南宁宾阳职业技术学校_FLTE1800基站_F_3', 'PROVINCE_ID': '110',
                     'CITY_ID': '11001', 'DISTRICT_ID': '1100126', 'LONGITUDE': '108.855926', 'LATITUDE': '23.236786',
                     'RELATED_BBU_ID': '46001698043', 'RELATED_CELL': '110.698043.3', 'PHY_ID': '1100126_00425',
                     'RRU_MODEL': '1', 'RRU_PORT': '1', 'TX_RX_MODE': '3'}
        para_dict['objectId'] = '110.110.698043.3'
        para_dict['RRU_ID'] = '110.698043.3'
        para_dict['LC_NAME'] = 'GX南宁宾阳职业技术学校_FLTE1800基站_F_3'
        para_dict['RELATED_BBU_ID'] = '46001698043'
        para_dict['RELATED_CELL'] = '110.698043.3'
        para_dict['PHY_ID'] = '1100126_00425'
        para_dict['RRU_MODEL'] = '1'
        para_dict['RRU_PORT'] = '1'
        para_dict['TX_RX_MODE'] = '3'
        # para_dict['PROVINCE_ID'] = '110',


        cityid = {"南宁市": "11001",
                  "柳州市": "11002",
                  "桂林市": "11003",
                  "梧州市": "11004",
                  "北海市": "11005",
                  "防城港市": "11006",
                  "钦州市": "11007",
                  "贵港市": "11008",
                  "玉林市": "11009",
                  "百色市": "11010",
                  "贺州市": "11011",
                  "河池市": "11012",
                  "来宾市": "11013",
                  "崇左市": "11014", }
        districtid = {
            "兴宁区": "1100102",
            "青秀区": "1100103",
            "江南区": "1100105",
            "西乡塘区": "1100107",
            "良庆区": "1100108",
            "邕宁区": "1100109",
            "武鸣县": "1100122",
            "隆安县": "1100123",
            "马山县": "1100124",
            "上林县": "1100125",
            "宾阳县": "1100126",
            "横县": "1100127",
            "城中区": "1100202", "鱼峰区": "1100203", "柳南区": "1100204", "柳北区": "1100205", "柳江县": "1100221", "柳城县": "1100222",
            "鹿寨县": "1100223", "融安县": "1100224", "融水苗族自治县": "1100225", "三江侗族自治县": "1100226", "秀峰区": "1100302",
            "叠彩区": "1100303", "象山区": "1100304", "七星区": "1100305", "雁山区": "1100311", "阳朔县": "1100321", "临桂县": "1100322",
            "灵川县": "1100323", "全州县": "1100324", "兴安县": "1100325", "永福县": "1100326", "灌阳县": "1100327",
            "龙胜各族自治县": "1100328", "资源县": "1100329", "平乐县": "1100330", "荔浦县": "1100331", "恭城瑶族自治县": "1100332",
            "万秀区": "1100403", "蝶山区": "1100404", "长洲区": "1100405", "苍梧县": "1100421", "藤县": "1100422", "蒙山县": "1100423",
            "岑溪市": "1100481", "海城区": "1100502", "银海区": "1100503", "铁山港区": "1100512", "合浦县": "1100521", "港口区": "1100602",
            "防城区": "1100603", "上思县": "1100621", "东兴市": "1100681", "钦南区": "1100702", "钦北区": "1100703", "灵山县": "1100721",
            "浦北县": "1100722", "港北区": "1100802", "港南区": "1100803", "覃塘区": "1100804", "平南县": "1100821", "桂平市": "1100881",
            "玉州区": "1100902", "容县": "1100921", "陆川县": "1100922", "博白县": "1100923", "兴业县": "1100924", "北流市": "1100981",
            "右江区": "1101002", "田阳县": "1101021", "田东县": "1101022", "平果县": "1101023", "德保县": "1101024", "靖西县": "1101025",
            "那坡县": "1101026", "凌云县": "1101027", "乐业县": "1101028", "田林县": "1101029", "西林县": "1101030",
            "隆林各族自治县": "1101031", "八步区": "1101102", "昭平县": "1101121", "钟山县": "1101122", "富川瑶族自治县": "1101123",
            "平桂区": "1101124", "金城江区": "1101202", "南丹县": "1101221", "天峨县": "1101222", "凤山县": "1101223", "东兰县": "1101224",
            "罗城仫佬族自治县": "1101225", "环江毛南族自治县": "1101226", "巴马瑶族自治县": "1101227", "都安瑶族自治县": "1101228",
            "大化瑶族自治县": "1101229", "宜州市": "1101281", "兴宾区": "1101302", "忻城县": "1101321", "象州县": "1101322",
            "武宣县": "1101323", "金秀瑶族自治县": "1101324", "合山市": "1101381", "江洲区": "1101402", "扶绥县": "1101421",
            "宁明县": "1101422", "龙州县": "1101423", "大新县": "1101424", "天等县": "1101425", "凭祥市": "1101481"}

        para_dict['CITY_ID'] = cityid[self.city]
        para_dict['DISTRICT_ID'] = districtid[self.district]
        para_dict['LONGITUDE'] = self.lon
        para_dict['LATITUDE'] = self.lat
        try:
            modify_nocheck(para_dict)
        except:
            raise ValueError('input error!')


class Antenna(models.Model):
    antennaid = models.CharField(max_length=50)
    antennaid1 = models.CharField(max_length=50)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    physicalstationid = models.CharField(max_length=20)
    rruid = models.CharField(max_length=100)
    cellid1 = models.CharField(max_length=100)
    directionangle = models.FloatField(blank=True, null=True)
    antennaheight = models.FloatField(blank=True, null=True)
    electricaldowntilt = models.CharField(max_length=20)
    mechanicaltilt = models.CharField(max_length=20)
    antennatypes = models.CharField(max_length=20)
    beautifytypes = models.CharField(max_length=20)
    antennafactory = models.CharField(max_length=100)
    antennamodel = models.CharField(max_length=100)
    antennanum = models.CharField(max_length=20)
    horizontalpowerangle = models.CharField(max_length=20)
    verticalpowerangle = models.CharField(max_length=20)
    antennagain = models.CharField(max_length=20)
    picture1 = models.CharField(max_length=20)
    picture2 = models.CharField(max_length=20)
    picture3 = models.CharField(max_length=20)
    picture4 = models.CharField(max_length=20)
    towermast = models.CharField(max_length=20)
    txrxmod = models.CharField(max_length=20)
    verticalrange = models.CharField(max_length=20)
    install = models.CharField(max_length=20)

    def init1(self, *args):
        # super(Antenna, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.antennaid = args[0]
                self.antennaid1 = args[1]
                self.province = args[2]
                self.city = args[3]
                self.district = args[4]
                self.lon = args[5]
                self.lat = args[6]
                self.physicalstationid = args[7]
                self.rruid = args[8]
                self.cellid1 = args[9]
                self.directionangle = args[10]
                self.antennaheight = args[11]
                self.electricaldowntilt = args[12]
                self.mechanicaltilt = args[13]
                self.antennatypes = args[14]
                self.beautifytypes = args[15]
                self.antennafactory = args[16]
                self.antennamodel = args[17]
                self.antennanum = args[18]
                self.horizontalpowerangle = args[19]
                self.verticalpowerangle = args[20]
                self.antennagain = args[21]
                self.picture1 = args[22]
                self.picture2 = args[23]
                self.picture3 = args[24]
                self.picture4 = args[25]
                self.towermast = args[26]
                self.txrxmod = args[27]
                self.verticalrange = args[28]
                self.install = args[29]
        return self


class Cell2scenes(models.Model):
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    scenesid = models.CharField(max_length=50)
    cellid1 = models.CharField(max_length=30)
    networktype = models.CharField(max_length=20)

    def init1(self, *args):
        # super(Cell2scenes, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.province = args[0]
                self.city = args[1]
                self.scenesid = args[2]
                self.cellid1 = args[3]
                self.networktype = args[4]
        return self


class Scenes(models.Model):
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    scenesid = models.CharField(max_length=50)
    scenesname = models.CharField(max_length=50)
    parentscenes = models.CharField(max_length=50)
    scenesdescription = models.CharField(max_length=1000)
    scenesrange = models.CharField(max_length=3000)
    sceneslon = models.FloatField(blank=True, null=True)
    sceneslat = models.FloatField(blank=True, null=True)
    firstscenes = models.CharField(max_length=50)
    secondscenes = models.CharField(max_length=50)
    hotregion = models.CharField(max_length=50)
    vitalarea = models.CharField(max_length=50)
    population = models.FloatField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    cell2g = models.CharField(max_length=50)
    cell3g = models.CharField(max_length=50)
    cell4g = models.CharField(max_length=50)
    carrier2g = models.CharField(max_length=50)
    carrier3g = models.CharField(max_length=50)
    carrier4g = models.CharField(max_length=50)
    fpoint2g = models.CharField(max_length=200)
    fpoint3g = models.CharField(max_length=100)
    fpoint4g = models.CharField(max_length=100)
    mobilecover2g = models.CharField(max_length=50)
    mobilecover3g = models.CharField(max_length=50)
    mobilecover4g = models.CharField(max_length=50)
    mobilefpoint = models.CharField(max_length=50)
    telecomcover2g = models.CharField(max_length=50)
    telecomcover3g = models.CharField(max_length=50)
    telecomcover4g = models.CharField(max_length=50)
    telecomfpoint = models.CharField(max_length=50)
    sceneslevel = models.CharField(max_length=50)
    customize1 = models.CharField(max_length=50)
    customize2 = models.CharField(max_length=50)

    def init1(self, *args):
        # super(Scenes, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.province = args[0]
                self.city = args[1]
                self.district = args[2]
                self.scenesid = args[3]
                self.scenesname = args[4]
                self.parentscenes = args[5]
                self.scenesdescription = args[6]
                self.scenesrange = args[7]
                self.sceneslon = args[8]
                self.sceneslat = args[9]
                self.firstscenes = args[10]
                self.secondscenes = args[11]
                self.hotregion = args[12]
                self.vitalarea = args[13]
                self.population = args[14]
                self.area = args[15]
                self.cell2g = args[16]
                self.cell3g = args[17]
                self.cell4g = args[18]
                self.carrier2g = args[19]
                self.carrier3g = args[20]
                self.carrier4g = args[21]
                self.fpoint2g = args[22]
                self.fpoint3g = args[23]
                self.fpoint4g = args[24]
                self.mobilecover2g = args[25]
                self.mobilecover3g = args[26]
                self.mobilecover4g = args[27]
                self.mobilefpoint = args[28]
                self.telecomcover2g = args[29]
                self.telecomcover3g = args[30]
                self.telecomcover4g = args[31]
                self.telecomfpoint = args[32]
                self.sceneslevel = args[33]
                self.customize1 = args[34]
                self.customize2 = args[35]
        return self


class Enodeb(models.Model):
    enodebname = models.CharField(max_length=60)
    enodebomcidentify = models.CharField(max_length=60)
    enodebomcname = models.CharField(max_length=60)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    villages = models.CharField(max_length=20)
    enodebid = models.CharField(max_length=20)
    enodebid2 = models.CharField(max_length=20)
    enodebid3 = models.CharField(max_length=20)
    enodebdn = models.CharField(max_length=20)
    emsid = models.CharField(max_length=30)
    mmeid = models.CharField(max_length=80)
    sgwid = models.CharField(max_length=30)
    factory = models.CharField(max_length=20)
    worktypes = models.CharField(max_length=20)
    updatatime = models.CharField(max_length=30)
    antennanumb = models.CharField(max_length=20)
    antennanumb2g = models.CharField(max_length=20)
    antennanumb3g = models.CharField(max_length=20)
    antennanumb23g = models.CharField(max_length=20)
    physicalstationnumb = models.CharField(max_length=20)
    physicalstationnumb2g = models.CharField(max_length=20)
    physicalstationnumb3g = models.CharField(max_length=20)
    physicalstationnumb23g = models.CharField(max_length=20)
    sourcetypes = models.CharField(max_length=20)
    commonmode = models.CharField(max_length=20)
    unittype = models.CharField(max_length=50)
    hwversion = models.CharField(max_length=50)
    swversion = models.CharField(max_length=50)
    swbugversion = models.CharField(max_length=50)
    s1ubandwidth = models.CharField(max_length=20)
    enodebbandwidth1 = models.CharField(max_length=20)
    enodebbandwidth2 = models.CharField(max_length=20)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    Carrier = models.CharField(max_length=20)
    Sectortype = models.CharField(max_length=20)
    bbunumb = models.CharField(max_length=20)
    rrunumb = models.CharField(max_length=20)
    rrunumb24G = models.CharField(max_length=20)
    repeater = models.CharField(max_length=20)
    bstype = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    bslevel = models.CharField(max_length=20)
    mcc = models.CharField(max_length=20)
    mnc = models.CharField(max_length=20)
    enodebcell = models.CharField(max_length=20)
    enodebip = models.CharField(max_length=50)
    towerdelivery = models.CharField(max_length=20)
    towerlocation = models.CharField(max_length=20)
    towerlevel = models.CharField(max_length=20)
    sharetelecom = models.CharField(max_length=20)
    builder = models.CharField(max_length=20)
    share = models.CharField(max_length=20)
    sharebs = models.CharField(max_length=20)
    customize1 = models.CharField(max_length=50)
    customize2 = models.CharField(max_length=50)
    customize3 = models.CharField(max_length=50)
    customize4 = models.CharField(max_length=50)
    customize5 = models.CharField(max_length=50)
    customize6 = models.CharField(max_length=50)
    customize7 = models.CharField(max_length=50)
    customize8 = models.CharField(max_length=50)
    customize9 = models.CharField(max_length=50)
    customize10 = models.CharField(max_length=50)

    def init1(self, *args):
        # super(Enodeb, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.enodebname = args[0]
                self.enodebomcidentify = args[1]
                self.enodebomcname = args[2]
                self.province = args[3]
                self.city = args[4]
                self.district = args[5]
                self.villages = args[6]
                self.enodebid = args[7]
                self.enodebid2 = args[8]
                self.enodebid3 = args[9]
                self.enodebdn = args[10]
                self.emsid = args[11]
                self.mmeid = args[12]
                self.sgwid = args[13]
                self.factory = args[14]
                self.worktypes = args[15]
                self.updatatime = args[16]
                self.antennanumb = args[17]
                self.antennanumb2g = args[18]
                self.antennanumb3g = args[19]
                self.antennanumb23g = args[20]
                self.physicalstationnumb = args[21]
                self.physicalstationnumb2g = args[22]
                self.physicalstationnumb3g = args[23]
                self.physicalstationnumb23g = args[24]
                self.sourcetypes = args[25]
                self.commonmode = args[26]
                self.unittype = args[27]
                self.hwversion = args[28]
                self.swversion = args[29]
                self.swbugversion = args[30]
                self.s1ubandwidth = args[31]
                self.enodebbandwidth1 = args[32]
                self.enodebbandwidth2 = args[33]
                self.lon = args[34]
                self.lat = args[35]
                self.Carrier = args[36]
                self.Sectortype = args[37]
                self.bbunumb = args[38]
                self.rrunumb = args[39]
                self.rrunumb24G = args[40]
                self.repeater = args[41]
                self.bstype = args[42]
                self.location = args[43]
                self.bslevel = args[44]
                self.mcc = args[45]
                self.mnc = args[46]
                self.enodebcell = args[47]
                self.enodebip = args[48]
                self.towerdelivery = args[49]
                self.towerlocation = args[50]
                self.towerlevel = args[51]
                self.sharetelecom = args[52]
                self.builder = args[53]
                self.share = args[54]
                self.sharebs = args[55]
                self.customize1 = args[56]
                self.customize2 = args[57]
                self.customize3 = args[58]
                self.customize4 = args[59]
                self.customize5 = args[60]
                self.customize6 = args[61]
                self.customize7 = args[62]
                self.customize8 = args[63]
                self.customize9 = args[64]
                self.customize10 = args[65]

        return self


class Rru(models.Model):
    rruid = models.CharField(max_length=50)
    rruname = models.CharField(max_length=200)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    bbuid = models.CharField(max_length=50)
    cellid1 = models.CharField(max_length=50)
    physicalstationid = models.CharField(max_length=50)
    rrutypes = models.CharField(max_length=20)
    rruport = models.CharField(max_length=20)
    txrxtypes = models.CharField(max_length=20)

    def init1(self, *args):
        # super(Rru, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.rruid = args[0]
                self.rruname = args[1]
                self.province = args[2]
                self.city = args[3]
                self.district = args[4]
                self.lon = args[5]
                self.lat = args[6]
                self.bbuid = args[7]
                self.cellid1 = args[8]
                self.physicalstationid = args[9]
                self.rrutypes = args[10]
                self.rruport = args[11]
                self.txrxtypes = args[12]
        return self


class Bbu(models.Model):
    bbuid = models.CharField(max_length=50)
    bbuname = models.CharField(max_length=100)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    factory = models.CharField(max_length=20)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    enodebid3 = models.CharField(max_length=50)
    physicalstationid = models.CharField(max_length=50)
    unittype = models.CharField(max_length=50)

    def init1(self, *args):
        # super(Bbu, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.bbuid = args[0]
                self.bbuname = args[1]
                self.province = args[2]
                self.city = args[3]
                self.district = args[4]
                self.factory = args[5]
                self.lon = args[6]
                self.lat = args[7]
                self.enodebid3 = args[8]
                self.physicalstationid = args[9]
                self.unittype = args[10]
        return self


class Physicalstation(models.Model):
    physicalstationid = models.CharField(max_length=50)
    physicalstationname = models.CharField(max_length=100)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    fulladdress = models.CharField(max_length=100)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    altitude = models.CharField(max_length=20)
    isboundary = models.CharField(max_length=20)

    def init1(self, *args):
        # super(Physicalstation, self).__init__()
        if args:
            if type(args[0]) is list:  # object is being created, thus no primary key field yet
                args = args[0]
                self.physicalstationid = args[0]
                self.physicalstationname = args[1]
                self.province = args[2]
                self.city = args[3]
                self.district = args[4]
                self.fulladdress = args[5]
                self.lon = args[6]
                self.lat = args[7]
                self.altitude = args[8]
                self.isboundary = args[9]
        return self
