"""
alloy deals with different types of supply chain data. today, we are going to write a preprocessor for shipment notice files. 
A shipment notice file gets sent when a manufacturer fulfills one or more orders from a retailer. It is a key input to the retailer's warehouse management process.
 the shipment notice file reflects the information hierarchy of the shipments. each manufacturer can have a different hierarchy. which depends on the type of products and other factors. COmmon hierarchies include:
    A shipment consists of different trucks. where each of the trucks fulfills multiple orders, and each order contains multiple packages(hierarchy: Truck> order> package)
    A shipment gets delivered with multiple airplanes. each airplane fultills multiple orders, and each order contains multiple packages for a particular item(hierarchy: Airplane > order>item>package)
    The order in which the level types appear in the file defines the hierarchy and each file has exactly one hierarchy(if you see airplane > order> package, the you will not suddenly see truck>order>item>package)
    our pre-processor should make the informaiton hierarchy explicit by taking each record and printint it so that it refers to its parent's record in the hierarchy. the output expects n lines containing the augmented records:
    input: [ID:LEVEL:DESCRIPTION]
    output_list [parent ID: ID: level type: DESCRIPTION]

"""
class Solution:
    def alloy_order(self, input_file):
        hierarchy1 = {"T":0,"O":1,"P":2}
        hierarchy2 = {"A":0,"O":1,"I":2,"P":3}
        #each record has a ID, and a hierarchy level and a description
        #input_list ["ID:LEVEL:DESCRIPTION"]
        #output_list ["parent ID, ID, level, DESCRIPTION"]
        def parse_file(file):
            #return the list
            file_handle = open(file, "r")
            records_num = int(file_handle.readline())
            input_list = file_handle.readlines()
            return input_list

        def hierarchy_build(input_list):
            #return a list of info with the output_list's format
            input = []
            for record in input_list:
                parsed_record = record.split(":")
                description = "".join(parsed_record[2:])
                current = parsed_record[:2]
                current.append(description)
                input.append(current)
            
                #input: [[ID, LEVEL, DESCRIPTION],[ID, LEVEL, DESCRIPTION],...,[ID, LEVEL, DESCRIPTION]]
            if input[0][1] == "T":
                hierarchy = hierarchy1
            else:
                hierarchy = hierarchy2
            all_levels = []
            ans = []
            for item in input:
                #ID, level, description
                #list of list
                level = item[1]
                if hierarchy[level] == len(all_levels):
                    if all_levels:
                        parent = all_levels[-1]
                    else:
                        parent = 0
                    all_levels.append(item[0])
                else:
                    parent_level = hierarchy[level]-1
                    parent = all_levels[parent_level]
                new = []
                new.append(parent)
                new+=item
                ans.append(new)
            return ans
        input_list = parse_file(input_file)
        return hierarchy_build(input_list)
print(Solution().alloy_order("tests/alloy.txt"))









