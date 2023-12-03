


rentdays = int(input("How many days rent?"))
kmtravel = int(input("how many km traveled?"))
rentdaypayment = 60
kmpayment = 0.15
totalpayment = (rentdaypayment * rentdays) + (kmtravel * kmpayment)
print("total payment for rent is ${:.2f}".format(totalpayment))
