import os


if __name__ == '__main__':
    folder_name = repr(os.getcwd()).replace("'", "")
    file_name = "".join([folder_name, r"\\SSS.dat"])
    with open(file_name, 'r+') as f:
        new_file = []
        lines = f.readlines()
        string_incorrect = "ЗД J=11"
        string_required = "ЗД J= 5"
        string_stop = "J= 6"
        for line in lines:
            if string_stop in line:
                break
            condition = string_incorrect in line
            if condition:
                line = line.replace(string_incorrect, string_required)
            new_file.append(line)
        f.seek(0)
        f.writelines(new_file)