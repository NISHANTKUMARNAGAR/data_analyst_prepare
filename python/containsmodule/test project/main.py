if __name__=="__main__":
    try:
        import utilities
        from utilities.calculations import calcmax as camax
        import utilities.validation
    except ModuleNotFoundError:
        print("requested module was not found")
    except ImportError:
        print("import operation failed")
    else:
        print(dir(utilities))
        print(utilities.validation.__name__)
        print(utilities.validation.__file__)
