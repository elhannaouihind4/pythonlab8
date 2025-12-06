import utils

def test_moyenne():
    """Test de la fonction moyenne."""
    assert utils.moyenne([10, 12, 14]) == 12.0
    assert utils.moyenne([]) == 0
    assert utils.moyenne([20]) == 20.0
    print("test_moyenne passé")

def test_est_admis():
    """Test de la fonction est_admis."""
    assert utils.est_admis(12) == True
    assert utils.est_admis(8) == False
    assert utils.est_admis(10) == True  
    assert utils.est_admis(15, seuil=12) == True
    print(" test_est_admis passé")

if __name__ == "__main__":
    test_moyenne()
    test_est_admis()
    print("\n Tous les tests sont passés !")