def PrintModels(UnprintedDesigns,CompletedModels):
    while UnprintedDesigns:
        CurrentDesign=UnprintedDesigns.pop()
        print("Printing model:"+ CurrentDesign)
        CompletedModels.append(CurrentDesign)

def ShowCompletedModels(CompletedModels):
    print("\nThe following models have been printed:")
    for CompeletedModel in CompletedModels:
        print(CompeletedModel)
UnprintedDesigns=['IPhone Case','Robot Pendant','Dechedron']
CompletedModels=[]
PrintModels(UnprintedDesigns[:],CompletedModels)
ShowCompletedModels(CompletedModels)
print(UnprintedDesigns)
print(CompletedModels)
