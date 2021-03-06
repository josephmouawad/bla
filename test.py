class DocPlanNode:
	def __init__(self , listargs):
		self.name = listargs[0];
		self.relation = listargs[1];
		self.children = listargs[2];
		self.message = listargs[3];
		self.visited = listargs[4];



DocPlan = {
	"route" : DocPlanNode(["route", "sequence", ["history","prefClasses","optimalPlan","alternativePlans"], "", False]),

	"history" : DocPlanNode(["route", "sequence", ["completedClassesMSG", "gpaMSG"], "", False]),
	"completedClassesMSG" : DocPlanNode(["route", "sequence", [], "", False]),
	"gpaMSG" : DocPlanNode(["route", "sequence", [], "",Fasle]),

	"prefClasses" : DocPlanNode(["route", "sequence", ["prefClassesAvailabilityMSG", "prefPreReqMSG"], "", False]),
	"prefClassesAvailabilityMSG" : DocPlanNode(["route", "sequence", [], "", False]),
	"prefPreReqMSG" : DocPlanNode(["route", "sequence", [], "", False]),

	"optimalPlan" : DocPlanNode(["route", "sequence", [], "", False]),
	
	"alternativePlans" : DocPlanNode(["route", "sequence", [], "", False])	
};

for k,v in DocPlan.items():
	print(k +  " " + str(v.visited));