import unittest
import sqlite3
import hw2_db_sql as hw


class Test_SQLStatements(unittest.TestCase):

    def test_question0(self):
        self.assertEqual(hw.question0(), [(1, 'Eastern'), (2, 'Western'), (3, 'Northern'), (4, 'Southern')])

    def test_question1(self):
        self.assertEqual(hw.question1(), [('01581', 'Westboro', 1), ('01730', 'Bedford', 1), ('01833', 'Georgetow', 1), ('02116', 'Boston', 1), ('02139', 'Cambridge', 1), ('02184', 'Braintree', 1), ('02903', 'Providence', 1), ('03049', 'Hollis', 3), ('03801', 'Portsmouth', 3), ('06897', 'Wilton', 1), ('07960', 'Morristown', 1), ('08837', 'Edison', 1), ('10019', 'New York', 1), ('10038', 'New York', 1), ('11747', 'Mellvile', 1), ('14450', 'Fairport', 1), ('19428', 'Philadelphia', 3), ('19713', 'Neward', 1), ('20852', 'Rockville', 1), ('27403', 'Greensboro', 1), ('27511', 'Cary', 1), ('29202', 'Columbia', 4), ('30346', 'Atlanta', 4), ('31406', 'Savannah', 4), ('32859', 'Orlando', 4), ('33607', 'Tampa', 4), ('40222', 'Louisville', 1), ('44122', 'Beachwood', 3), ('45839', 'Findlay', 3), ('48075', 'Southfield', 3), ('48084', 'Troy', 3), ('48304', 'Bloomfield Hills', 3), ('53404', 'Racine', 3), ('55113', 'Roseville', 3), ('55439', 'Minneapolis', 3), ('60179', 'Hoffman Estates', 2), ('60601', 'Chicago', 2), ('72716', 'Bentonville', 4), ('75234', 'Dallas', 4), ('78759', 'Austin', 4), ('80202', 'Denver', 2), ('80909', 'Colorado Springs', 2), ('85014', 'Phoenix', 2), ('85251', 'Scottsdale', 2), ('90405', 'Santa Monica', 2), ('94025', 'Menlo Park', 2), ('94105', 'San Francisco', 2), ('95008', 'Campbell', 2), ('95054', 'Santa Clara', 2), ('95060', 'Santa Cruz', 2), ('98004', 'Bellevue', 2), ('98052', 'Redmond', 2), ('98104', 'Seattle', 2)])
    
    def test_question2(self):
        self.assertEqual(hw.question2(), [(9,)])
    
    def test_question3(self):
        self.assertEqual(hw.question3(), [(77, 'Original Frankfurter grüne Soße', 12, 2, '12 boxes', 13, 32, 0, 15, 0), (76, 'Lakkalikööri', 23, 1, '500 ml', 18, 57, 0, 20, 0), (75, 'Rhönbräu Klosterbier', 12, 1, '24 - 0.5 l bottles', 7.75, 125, 0, 25, 0), (74, 'Longlife Tofu', 4, 7, '5 kg pkg.', 10, 4, 20, 5, 0), (73, 'Röd Kaviar', 17, 8, '24 - 150 g jars', 15, 101, 0, 5, 0), (72, 'Mozzarella di Giovanni', 14, 4, '24 - 200 g pkgs.', 34.8, 14, 0, 0, 0), (71, 'Flotemysost', 15, 4, '10 - 500 g pkgs.', 21.5, 26, 0, 0, 0), (70, 'Outback Lager', 7, 1, '24 - 355 ml bottles', 15, 15, 10, 30, 0), (69, 'Gudbrandsdalsost', 15, 4, '10 kg pkg.', 36, 26, 0, 15, 0), (68, 'Scottish Longbreads', 8, 3, '10 boxes x 8 pieces', 12.5, 6, 10, 15, 0)])
    
    def test_question4(self):
        self.assertEqual(hw.question4(), [('Côte de Blaye', 263.5), ('Thüringer Rostbratwurst', 123.79), ('Mishi Kobe Niku', 97)])
    
    def test_question5(self):
        self.assertEqual(hw.question5(), [('Queso Manchego La Pastora', 38, 86), ('Tunnbröd', 9, 61), ('NuNuCa Nuß-Nougat-Creme', 14, 76), ('Chartreuse verte', 18, 69), ("Jack's New England Clam Chowder", 9.65, 85), ('Spegesild', 12, 95), ('Valkoinen suklaa', 16.25, 65), ('Escargots de Bourgogne', 13.25, 62), ('Raclette Courdavault', 55, 79), ('Louisiana Fiery Hot Pepper Sauce', 21.05, 76)])

    def test_question6(self):
        self.assertEqual(hw.question6(), [('Chang',), ('Aniseed Syrup',), ('Queso Cabrales',), ("Sir Rodney's Scones",), ('Nord-Ost Matjeshering',), ('Gorgonzola Telino',), ('Mascarpone Fabioli',), ('Gravad lax',), ('Ipoh Coffee',), ('Rogede sild',), ('Chocolade',), ('Maxilaku',), ('Gnocchi di nonna Alice',), ('Wimmers gute Semmelknödel',), ('Louisiana Hot Spiced Okra',), ('Scottish Longbreads',), ('Outback Lager',), ('Longlife Tofu',)])
    
    def test_question7(self):
        self.assertEqual(hw.question7(), [(10251,), (10334,), (10450,), (10459,), (10478,), (10546,), (10806,), (10814,), (10843,), (10850,)])
    
    def test_question8(self):
        self.assertEqual(hw.question8(), [('Around the Horn', 'Thomas Hardy'), ('Consolidated Holdings', 'Elizabeth Brown'), ('Eastern Connection', 'Ann Devon'), ('North/South', 'Simon Crowther'), ('Seven Seas Imports', 'Hari Kumar')])
    
    def test_question9(self):
        self.assertEqual(hw.question9(), [('Chai', 18), ('Chang', 19), ('Guaraná Fantástica', 4.5), ('Sasquatch Ale', 14), ('Steeleye Stout', 18), ('Côte de Blaye', 263.5), ('Chartreuse verte', 18), ('Ipoh Coffee', 46), ('Laughing Lumberjack Lager', 14), ('Outback Lager', 15), ('Rhönbräu Klosterbier', 7.75), ('Lakkalikööri', 18)])
    
    def test_question10(self):
        self.assertEqual(hw.question10(), [('Mishi Kobe Niku',), ('Alice Mutton',), ('Thüringer Rostbratwurst',), ('Perth Pasties',)])
    
    def test_question11(self):
        self.assertEqual(hw.question11(), [(10249, 'Michael', 'Suyama'), (10260, 'Margaret', 'Peacock'), (10267, 'Margaret', 'Peacock'), (10273, 'Janet', 'Leverling'), (10277, 'Andrew', 'Fuller'), (10279, 'Laura', 'Callahan'), (10284, 'Margaret', 'Peacock'), (10285, 'Nancy', 'Davolio'), (10286, 'Laura', 'Callahan'), (10301, 'Laura', 'Callahan'), (10312, 'Andrew', 'Fuller'), (10313, 'Andrew', 'Fuller'), (10323, 'Margaret', 'Peacock'), (10325, 'Nancy', 'Davolio'), (10337, 'Margaret', 'Peacock'), (10342, 'Margaret', 'Peacock'), (10343, 'Margaret', 'Peacock'), (10345, 'Andrew', 'Fuller'), (10348, 'Margaret', 'Peacock'), (10356, 'Michael', 'Suyama'), (10361, 'Nancy', 'Davolio'), (10363, 'Margaret', 'Peacock'), (10391, 'Janet', 'Leverling'), (10396, 'Nancy', 'Davolio'), (10407, 'Andrew', 'Fuller'), (10418, 'Margaret', 'Peacock'), (10438, 'Janet', 'Leverling'), (10446, 'Michael', 'Suyama'), (10451, 'Margaret', 'Peacock'), (10456, 'Laura', 'Callahan'), (10457, 'Andrew', 'Fuller'), (10468, 'Janet', 'Leverling'), (10488, 'Laura', 'Callahan'), (10497, 'Robert', 'King'), (10501, 'Anne', 'Dodsworth'), (10506, 'Anne', 'Dodsworth'), (10508, 'Nancy', 'Davolio'), (10509, 'Margaret', 'Peacock'), (10513, 'Robert', 'King'), (10515, 'Andrew', 'Fuller'), (10522, 'Margaret', 'Peacock'), (10527, 'Robert', 'King'), (10534, 'Laura', 'Callahan'), (10536, 'Janet', 'Leverling'), (10540, 'Janet', 'Leverling'), (10542, 'Nancy', 'Davolio'), (10548, 'Janet', 'Leverling'), (10549, 'Steven', 'Buchanan'), (10554, 'Margaret', 'Peacock'), (10557, 'Anne', 'Dodsworth'), (10560, 'Laura', 'Callahan'), (10575, 'Steven', 'Buchanan'), (10580, 'Margaret', 'Peacock'), (10582, 'Janet', 'Leverling'), (10588, 'Andrew', 'Fuller'), (10592, 'Janet', 'Leverling'), (10593, 'Robert', 'King'), (10608, 'Margaret', 'Peacock'), (10614, 'Laura', 'Callahan'), (10623, 'Laura', 'Callahan'), (10630, 'Nancy', 'Davolio'), (10632, 'Laura', 'Callahan'), (10640, 'Margaret', 'Peacock'), (10643, 'Michael', 'Suyama'), (10651, 'Laura', 'Callahan'), (10653, 'Nancy', 'Davolio'), (10658, 'Margaret', 'Peacock'), (10668, 'Nancy', 'Davolio'), (10670, 'Margaret', 'Peacock'), (10675, 'Steven', 'Buchanan'), (10684, 'Janet', 'Leverling'), (10691, 'Andrew', 'Fuller'), (10692, 'Margaret', 'Peacock'), (10694, 'Laura', 'Callahan'), (10699, 'Janet', 'Leverling'), (10702, 'Margaret', 'Peacock'), (10717, 'Nancy', 'Davolio'), (10718, 'Nancy', 'Davolio'), (10721, 'Steven', 'Buchanan'), (10745, 'Anne', 'Dodsworth'), (10765, 'Janet', 'Leverling'), (10766, 'Margaret', 'Peacock'), (10772, 'Janet', 'Leverling'), (10779, 'Janet', 'Leverling'), (10788, 'Nancy', 'Davolio'), (10791, 'Michael', 'Suyama'), (10797, 'Robert', 'King'), (10799, 'Anne', 'Dodsworth'), (10817, 'Janet', 'Leverling'), (10825, 'Nancy', 'Davolio'), (10833, 'Michael', 'Suyama'), (10835, 'Nancy', 'Davolio'), (10845, 'Laura', 'Callahan'), (10849, 'Anne', 'Dodsworth'), (10853, 'Anne', 'Dodsworth'), (10859, 'Nancy', 'Davolio'), (10862, 'Laura', 'Callahan'), (10865, 'Andrew', 'Fuller'), (10878, 'Margaret', 'Peacock'), (10891, 'Robert', 'King'), (10893, 'Anne', 'Dodsworth'), (10929, 'Michael', 'Suyama'), (10934, 'Janet', 'Leverling'), (10938, 'Janet', 'Leverling'), (10945, 'Margaret', 'Peacock'), (10952, 'Nancy', 'Davolio'), (10956, 'Michael', 'Suyama'), (10962, 'Laura', 'Callahan'), (10967, 'Andrew', 'Fuller'), (10991, 'Nancy', 'Davolio'), (10996, 'Margaret', 'Peacock'), (10999, 'Michael', 'Suyama'), (11011, 'Janet', 'Leverling'), (11012, 'Nancy', 'Davolio'), (11020, 'Andrew', 'Fuller'), (11021, 'Janet', 'Leverling'), (11028, 'Andrew', 'Fuller'), (11036, 'Laura', 'Callahan'), (11046, 'Laura', 'Callahan'), (11058, 'Anne', 'Dodsworth'), (11067, 'Nancy', 'Davolio'), (11070, 'Andrew', 'Fuller')])
    
    def test_question12(self):
        self.assertEqual(hw.question12(), [(10248, '2012-07-04', 'Vins et alcools Chevalier'), (10249, '2012-07-05', 'Toms Spezialitäten'), (10250, '2012-07-08', 'Hanari Carnes'), (10251, '2012-07-08', 'Victuailles en stock'), (10252, '2012-07-09', 'Suprêmes délices'), (10253, '2012-07-10', 'Hanari Carnes')])


if __name__ == '__main__':
    unittest.main()